import argparse
from pathlib import Path
from typing import Iterable, List

from tqdm import tqdm

from data import ZIP_CODES, in_states, parse_zip_codes
from zip_code import ZIPCode


def create_map_url(zip_codes: Iterable[ZIPCode], title: str) -> str:
    return f"https://www.randymajors.com/p/customgmap.html?zips={','.join(str(z) for z in zip_codes)}&title={'+'.join(title.split())}"


def preprocess(zip_codes: Iterable[ZIPCode]) -> List[ZIPCode]:
    return list(filter(
        lambda z: in_states(z, ["TX"]),
        zip_codes
    ))


def main(f: str, radius: int, _map: bool, title: str) -> int:
    # Parse zip codes from file
    initial_zips = parse_zip_codes(Path(f).read_text())

    # Create set of all zip codes
    all_zips = set(initial_zips)

    if radius > 0:
        for z in tqdm(preprocess(ZIP_CODES.values())):
            if any(zip_code.distance(z) <= radius for zip_code in initial_zips):
                all_zips.add(z)

    if _map:
        # Print URL to map of zip code boundaries
        print(create_map_url(all_zips, title))
    else:
        # Print sorted set of all zip codes
        print("\n".join(sorted(str(z) for z in all_zips)))

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
