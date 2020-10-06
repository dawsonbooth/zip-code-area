import csv
import re
from pathlib import Path
from typing import List, Iterable

from zip_code import ZIPCode


def in_states(zip_code: ZIPCode, states: List[str]) -> bool:
    return zip_code.state in states

def preprocess(zip_codes: Iterable[ZIPCode]) -> List[ZIPCode]:
    return list(filter(
        lambda z: in_states(z, ["TX", "OK"]),
        zip_codes
    ))


def load_zip_codes(filename):
    reader = csv.reader(open(filename, "r"))
    next(reader)

    zip_codes = dict()

    for row in reader:
        zip_codes[row[0]] = ZIPCode(*row)

    return zip_codes


ZIP_CODES = load_zip_codes(str(
    Path(__file__).parent.joinpath("./zipcodes.csv").resolve()
))


def parse_zip_codes(body: str, key=lambda z: z.zip_code) -> List[ZIPCode]:
    return sorted(filter(lambda z: z is not None, (ZIP_CODES.get(z, None) for z in re.findall(r"[0-9]{5}", body))), key=key)
