import argparse
from pathlib import Path
from typing import Iterable, Iterator, List, Set

from tqdm import tqdm

from data import ZIP_CODES, in_states, parse_zip_codes, preprocess
from map import create_map_url
from zip_code import ZIPCode


def surrounding(zip_codes: List[ZIPCode], interior_zips: Iterable[ZIPCode], radius: int) -> Set[ZIPCode]:
    surrounding_zips = set()
    if radius > 0:
        for z in tqdm(zip_codes):
            if any(zip_code.distance(z) <= radius for zip_code in interior_zips):
                surrounding_zips.add(z)
    return surrounding_zips


def main(f: str, radius: int, _map: bool, title: str) -> int:
    # Parse zip codes from file
    interior_zips = set(parse_zip_codes(Path(f).read_text()))

    # Load all zip codes
    all_zips = list(preprocess(ZIP_CODES.values()))

    # Get surrounding zip codes
    combined_zips = interior_zips.union(
        surrounding(all_zips, interior_zips, radius))

    if _map:
        # Print URL to map of zip code boundaries
        print(create_map_url(combined_zips, title))
    else:
        # Print sorted set of all zip codes
        print("\n".join(sorted(str(z) for z in combined_zips)))

    # Finish with no errors
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('file', type=str,
                        help='Path to file that contains list of zip codes')
    parser.add_argument('--radius', type=int, default=0,
                        help='Search radius for surrounding zip codes')
    parser.add_argument('--map', action="store_true",
                        help="Provide URL to view zip code boundaries in a map")
    parser.add_argument('--title', type=str, default="Zip Codes",
                        help='Title for map of zip code boundaries')

    args = parser.parse_args()

    exit(main(args.file, args.radius, args.map, args.title))
