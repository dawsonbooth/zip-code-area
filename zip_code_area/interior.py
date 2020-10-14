import concurrent.futures
from typing import Iterable, List, Set

from tqdm import tqdm

from .data import ZIP_CODES, parse_zip_codes
from .map import create_map_url
from .zip_code import ZIPCode


def interior(zip_codes: List[ZIPCode], combined_zips: Iterable[ZIPCode], radius: int) -> Set[ZIPCode]:
    surrounding_zips = set()

    def check_zip(z: ZIPCode):
        if z not in combined_zips:
            for zip_code in combined_zips:
                if zip_code not in surrounding_zips and zip_code.distance(z) <= radius:
                    surrounding_zips.add(zip_code)

    if radius > 0:
        with tqdm(total=len(zip_codes)) as prog:
            with concurrent.futures.ThreadPoolExecutor() as e:
                remove_futures = (e.submit(check_zip, z) for z in zip_codes)
                for _ in concurrent.futures.as_completed(remove_futures):
                    prog.update(1)

    return set(z for z in combined_zips if z not in surrounding_zips)


def main(body: str, radius: int, _map: bool, title: str) -> int:
    # Parse zip codes from file
    combined_zips = parse_zip_codes(body)

    # Load all zip codes
    all_zips = list(ZIP_CODES.values())

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
