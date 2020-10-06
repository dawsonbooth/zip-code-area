import argparse
from pathlib import Path
from typing import Iterable

from data import parse_zip_codes
from zip_code import ZIPCode


def create_map_url(zip_codes: Iterable[ZIPCode], title: str) -> str:
    return f"https://www.randymajors.com/p/customgmap.html?zips={','.join(str(z) for z in zip_codes)}&title={'+'.join(title.split())}"


def main(f: str, title: str) -> int:
    # Parse zip codes from file
    zips = parse_zip_codes(Path(f).read_text())

    # Print URL to map of zip code boundaries
    print(create_map_url(zips, title))

    # Finish with no errors
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Provide URL to view zip code boundaries in a map')
    parser.add_argument('file', type=str,
                        help='Path to file that contains list of zip codes')
    parser.add_argument('--title', type=str, default="Zip Codes",
                        help='Title for map of zip code boundaries')

    args = parser.parse_args()

    exit(main(args.file, args.title))
