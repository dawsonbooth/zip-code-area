import argparse
import re
from pathlib import Path

from pyzipcode import ZipCodeDatabase

ZCDB = ZipCodeDatabase()


def parse_zip_codes(body: str, sort_key=str.lower):
    return sorted(re.findall(r"[0-9]{5}", body), key=sort_key)


def get_surrounding_zip_codes(zip_code: str, radius: int):
    for z in ZCDB.get_zipcodes_around_radius(zip_code, radius):
        yield z.zip


def main(f: str, radius: int) -> int:
    # Parse zip codes from file
    initial_zips = parse_zip_codes(Path(f).read_text())

    # Create set of all zip codes
    all_zips = set(initial_zips)
    for z in initial_zips:
        for s in get_surrounding_zip_codes(z, radius):
            all_zips.add(s)

    # Print sorted set of all zip codes
    print("\n".join(sorted(all_zips)))

    # Finish with no errors
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('file', type=str,
                        help='Path to file that contains list of zip codes')
    parser.add_argument('--radius', type=int, default=None,
                        help='Search radius for surrounding zip codes')
    args = parser.parse_args()

    exit(main(args.file, args.radius))
