#!/usr/bin/python3
"""Log parsing"""


import sys

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
counter = 0
total_size = 0
try:
    # read line by line
    for line in sys.stdin:
        try:
            tokens = line.split()
            status_code = int(tokens[-2])
            file_size = int(tokens[-1])
        except (IndexError, ValueError):
            # skip line if it doesn't have the right format
            print("Invalid line format:")
            continue

        # update stats
        total_size += file_size
        status_codes[status_code] += 1
        counter += 1

        if counter % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes.keys()):
                if status_codes[code] != 0:
                    print("{}: {}".format(code, status_codes[code]))

except Exception as err:
    pass

finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))
