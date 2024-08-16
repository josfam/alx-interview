#!/usr/bin/python3

"""Parsing logs from stdin, and printing summaries of the lines"""

import sys
import re

ip = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
date = r'\[(?P<date>\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{1,2}\.\d{1,6})\]'
get = r'"GET \/projects\/260 HTTP\/1.1"'
status_code = r'(?P<status_code>\d{3})?'
file = r'(?P<file_size>\d{1,4})'

pattern = f"{ip} - {date} {get} {status_code} {file}"

total_file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}


def print_summary() -> None:
    """Prints a summary of the total file size seen so far, and how many types
    of a particular status code have been seen
    """
    print(f'File size: {total_file_size}')
    for status_code, count in status_counts.items():
        print(f'{status_code}: {count}')


try:
    for count, line in enumerate(sys.stdin):
        if count > 0 and count % 10 == 0:
            print_summary()
        match = re.match(pattern, line)
        if match:
            total_file_size += int(match.group('file_size'))
            # count up the status codes
            try:
                status_counts[int(match.group('status_code'))] += 1
            except (ValueError, TypeError, KeyError):
                pass
except KeyboardInterrupt as e:
    print_summary()
