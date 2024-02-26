from sys import argv
from collections import Counter


def parse_log_line(line: str) -> dict:
    line = line.split(' ', 3)
    return {'date': line[0], 'time': line[1], 'level': line[2], 'message': line[3]}

print(parse_log_line('2024-01-22 08:30:01 INFO User logged in successfully.'))