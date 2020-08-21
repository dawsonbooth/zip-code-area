import csv

from zip_code import ZIP_Code


def is_acceptable(zip_code):
    return 72 <= zip_code and zip_code <= 76


def load_zip_codes(filename):
    reader = csv.reader(open(filename, "r"))
    next(reader)

    zip_codes = dict()

    for row in reader:
        if is_acceptable(int(row[0][:2])):
            zip_codes[row[0]] = ZIP_Code(*row)

    return zip_codes
