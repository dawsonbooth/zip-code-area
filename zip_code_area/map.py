from typing import Iterable

from .data import parse_zip_codes
from .zip_code import ZIPCode


def create_map_url(zip_codes: Iterable[ZIPCode], title: str) -> str:
    zips = ",".join(str(z) for z in zip_codes)
    return f"https://www.randymajors.com/p/customgmap.html?zips={zips}&title={title}"


def main(body: str, title: str) -> int:
    # Parse zip codes from file
    zips = parse_zip_codes(body)

    # Print URL to map of zip code boundaries
    print(create_map_url(zips, title))

    # Finish with no errors
    return 0
