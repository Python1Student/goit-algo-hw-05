from sys import argv
from collections import Counter


def parse_log_line(line: str) -> dict:
    line = line.split(' ', 3)
    return {'date': line[0], 'time': line[1], 'level': line[2], 'message': line[3]}


def load_logs(file_path: str) -> list:
    with open(file_path, 'r') as file:
        lines_list = [parse_log_line(line) for line in file.readlines()]
    return lines_list

print(load_logs('logfile.log'))