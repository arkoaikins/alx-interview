#!/usr/bin/python3
import sys
import re
from collections import Counter


total_size = 0
status_dict = Counter()
line_count = 0
possible_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)"  # nopep8


def print_statistics():
    """Prints the current statistics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_dict.items()):
        print("{}: {}".format(code, count))


try:
    for log in sys.stdin:
        line_count += 1
        match = re.search(pattern, log)

        if match:
            status_code, file_size = match.groups()
            if status_code.isdigit() and int(status_code) in possible_status_codes:  # nopep8
                status_dict[status_code] += 1
                total_size += int(file_size)

        if line_count % 10 == 0 or line_count == 1:
            print_statistics()

except KeyboardInterrupt:
    pass

# Print final statistics
print_statistics()
