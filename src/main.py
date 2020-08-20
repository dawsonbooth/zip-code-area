import argparse
import re
from pathlib import Path

from data import load_zip_codes

from typing import Iterable

from zip_code import ZIP_Code

from tqdm import tqdm

ZIP_CODES = load_zip_codes("data/zipcodes.csv")


def parse_zip_codes(body: str, key=lambda z: z.zip_code):
    return sorted((ZIP_CODES[z] for z in re.findall(r"[0-9]{5}", body)), key=key)


def get_surrounding_zip_codes(zip_code: ZIP_Code, radius: int):
    
    for z in tqdm(ZIP_CODES.values()):
        if zip_code.distance(z) <= radius:
            yield z


def create_map_url(zip_codes: Iterable, title: str):
    return f"https://www.randymajors.com/p/customgmap.html?zips={','.join(str(z) for z in zip_codes)}&title={'+'.join(title.split())}"


def main(f: str, radius: int, _map: bool, title: str) -> int:
    # Parse zip codes from file
    initial_zips = parse_zip_codes(Path(f).read_text())

    # Create set of all zip codes
    all_zips = set(initial_zips)

    if radius > 0:
        for z in tqdm(initial_zips):
            for s in get_surrounding_zip_codes(z, radius):
                all_zips.add(s)

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
