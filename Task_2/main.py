# Створємо генератор який оброблює переданий текст
def generator_numbers(text: str) -> float: # type: ignore
    # Перебираємо слова з тексту
    for word in text.split():
        # Перевіряємо чи слово є число
        if word.split('.')[0].isdigit(): 
            # Повертаємо число
            yield float(word)

# Створюємо функцію підрахунку доходу
def sum_profit(text: str, func: callable) -> float:
    return sum(func(text), 0.0)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

