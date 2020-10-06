import concurrent.futures
from pathlib import Path
from typing import Iterable, List, Set

from tqdm import tqdm

from .data import ZIP_CODES, parse_zip_codes, preprocess
from .map import create_map_url
from .zip_code import ZIPCode


def surrounding(zip_codes: List[ZIPCode], interior_zips: Iterable[ZIPCode], radius: int) -> Set[ZIPCode]:
    surrounding_zips = set()

    def check_zip(z: ZIPCode):
        if any(zip_code.distance(z) <= radius for zip_code in interior_zips):
            surrounding_zips.add(z)

    if radius > 0:
        with tqdm(total=len(zip_codes)) as prog:
            with concurrent.futures.ThreadPoolExecutor() as e:
                add_futures = (e.submit(check_zip, z) for z in zip_codes)
                for _ in concurrent.futures.as_completed(add_futures):
                    prog.update(1)

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
