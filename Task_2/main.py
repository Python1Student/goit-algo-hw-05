
def generator_numbers(text: str) -> float:  # Створємо генератор який оброблює переданий текст # type: ignore
    for word in text.split(): # Перебираємо слова з тексту
        if word.split('.')[0].isdigit(): # Перевіряємо чи слово є число
            yield float(word) # Повертаємо число


def sum_profit(text: str, func: callable) -> float: # Створюємо функцію підрахунку доходу
    return sum(func(text), 0.0)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

