import csv
import string
import sys
import os.path
import argparse

# Parse arguments
parser = argparse.ArgumentParser(
                    prog='find-diacritics',
                    description='Find records containing image links with non-ASCII characters',
                    epilog='Example: python find-diacritics -d , input.csv')
parser.add_argument('filename')
parser.add_argument('-d', '--delimiter', default=';')
args = parser.parse_args()

# Default values
DELIMITER = args.delimiter;
filename = args.filename

if not os.path.isfile(filename):
    print('File', filename, ' does not exist!')
    print('Enter: python ', sys.argv[0], ' filename.csv')
    exit()

def containsLinkWithDiacritics(record):
    for itemstring in record:
        if itemstring.startswith('http') or 'emco.cz' in itemstring or '.jpg' in itemstring:
            for char in itemstring:
                if not char in string.printable:
                    return True
    return False    


# Open file
with open(filename, 'r', encoding='utf-8') as csvfile:

    # Use CSV reader to parse
    reader = csv.reader(csvfile, delimiter=DELIMITER)

    # Test each record:
    for record in reader:
        if containsLinkWithDiacritics(record):
           print(DELIMITER.join(record))
