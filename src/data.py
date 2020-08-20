import csv

from zip_code import ZIP_Code


def load_zip_codes(filename):
    reader = csv.reader(open(filename, "r"))
    next(reader)

    zip_codes = dict()

    for row in reader:
        zip_codes[row[0]] = ZIP_Code(*row)

    return zip_codes
