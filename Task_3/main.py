from sys import argv
from collections import Counter


def parse_log_line(line: str) -> dict:
    line = line.split(' ', 3)  # Розділення рядка на список за пробілами, максимум 3 роздільники
    return {'date': line[0], 'time': line[1], 'level': line[2], 'message': line[3].strip()}  # Створення словника з датою, часом, рівнем та повідомленням


def load_logs(file_path: str) -> list:
    with open(file_path, 'r') as file:  # Відкриття файлу для читання
        lines_list = [parse_log_line(line) for line in file.readlines()]  # Створення списку словників, де кожен словник представляє рядок логу
    return lines_list  # Повернення списку рядків логу


def filter_logs_by_level(logs: list, level: str) -> list:
    level_logs = [f'{log['date']} {log['time']} {log['message']}' for log in logs if log['level'] == level.upper()]  # Відбір логів заданого рівня та форматування для виводу
    return level_logs  # Повернення списку відфільтрованих рядків


def count_logs_by_level(logs: list) -> dict:
    return Counter([log['level'] for log in logs])  # Підрахунок кількості логів за кожним рівнем


def display_log_counts(counts: dict) -> None:
    print(f'''{"Рівень логування":^18}| {"Кількість":^10}''')  # Вивід заголовка таблиці
    print('-' * 18 + '|' + '-' * 11)  # Вивід розділювача
    for key, value in counts.items():  # Ітерація по елементах словника
        print(f'''{key:^18}| {value:^10}''')  # Вивід кількості логів за кожним рівнем

    if len(argv) > 2:  # Перевірка наявності аргументів командного рядка
        print(f'\nДеталі логів для рівня {argv[2].upper()}:')  # Вивід інформації про рівень логування
        for line in filter_logs_by_level(logs, argv[2]):  # Вивід відфільтрованих логів
            print(line)


if __name__ == '__main__':  # Перевірка, чи цей скрипт запускається безпосередньо, а не імпортується в інший скрипт
    try:
        file_path = argv[1]  # Отримання шляху до файлу з аргументів командного рядка
        logs = load_logs(file_path)  # Завантаження рядків логів з файлу
        count = count_logs_by_level(logs)  # Підрахунок кількості логів за кожним рівнем
        display_log_counts(count)  # Вивід загальної кількості логів за кожним рівнем
    except:  # Обробка винятків
        print('\n' * 3 + 'ERROR' + '\n' * 3)  # Вивід повідомлення про помилку


