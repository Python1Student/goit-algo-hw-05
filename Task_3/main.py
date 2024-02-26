from sys import argv
from collections import Counter


def parse_log_line(line: str) -> dict:
    line = line.split(' ', 3)
    return {'date': line[0], 'time': line[1], 'level': line[2], 'message': line[3].strip()}


def load_logs(file_path: str = 'Task_3/logfile.log') -> list:
    with open(file_path, 'r') as file:
        lines_list = [parse_log_line(line) for line in file.readlines()]
    return lines_list


def filter_logs_by_level(logs: list, level: str) -> list:
    print(f'\nДеталі логів для рівня {level.upper()}:')
    level_logs = [f'{log['date']} {log['time']} {log['message']}' for log in logs if log['level'] == level.upper()]
    return level_logs


def count_logs_by_level(logs: list) -> dict:
    return Counter([log['level'] for log in logs])


def display_log_counts(counts: dict) -> None:
    print(f'''{"Рівень логування":^18}| {"Кількість":^10}''')
    print('-' * 18 + '|' + '-' * 11)
    for key, value in counts.items():
        print(f'''{key:^18}| {value:^10}''')

    if len(argv) > 2:
        for line in filter_logs_by_level(logs, argv[2]):
            print(line)


if __name__ == '__main__':    
    try:   
        file_path = argv[1]
        logs = load_logs(file_path)
        count = count_logs_by_level(logs)
        display_log_counts(count)
    except:
        print('\n' * 3 + 'ERROR' + '\n' * 3)

