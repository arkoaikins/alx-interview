#!/usr/bin/python3
import sys
import re

# store the status codes in a dictionary
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # to count the number lines


def print_statistics():
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


try:
    for line in sys.stdin:
        match = re.match(r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$', line)  # nopep8
        if match:
            status_code, file_size = match.groups()

            if status_code in status_codes_dict:
                status_codes_dict[status_code] += 1

            # update the  total size
            total_size += int(file_size)

            # update count of lines
            count += 1

            if count == 10:
                count = 0  # reset count
                print_statistics()

except KeyboardInterrupt:
    pass

finally:
    print_statistics()
