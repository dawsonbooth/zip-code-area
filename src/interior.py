import argparse
from pathlib import Path
from typing import Iterable, List, Set

from tqdm import tqdm

from data import ZIP_CODES, in_states, parse_zip_codes, preprocess
from map import create_map_url
from surrounding import surrounding
from zip_code import ZIPCode


def interior(zip_codes: List[ZIPCode], combined_zips: Iterable[ZIPCode], radius: int) -> Set[ZIPCode]:
    interior_zips = set(combined_zips)
    if radius > 0:
        for z in tqdm(zip_codes):
            if z not in combined_zips:
                for zip_code in combined_zips:
                    if zip_code in interior_zips and zip_code.distance(z) <= radius:
                        interior_zips.remove(zip_code)
    return interior_zips


def main(f: str, radius: int, _map: bool, title: str) -> int:
    # Parse zip codes from file
    combined_zips = parse_zip_codes(Path(f).read_text())

    # Load all zip codes
    all_zips = list(preprocess(ZIP_CODES.values()))

    # Get surrounding zip codes
    interior_zips = interior(all_zips, combined_zips, radius)

    if _map:
        # Print URL to map of zip code boundaries
        print(create_map_url(interior_zips, title))
    else:
        # Print sorted set of all zip codes
        print("\n".join(sorted(str(z) for z in interior_zips)))

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
