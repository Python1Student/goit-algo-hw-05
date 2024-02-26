def generator_numbers(text: str) -> float:
    text = text.split()  
    for word in text:
        if word.split('.')[0].isdigit():
            yield float(word)

def sum_profit(text: str, func) -> float:
    sum = 0.0
    func = func(text)
    for i in range(len(text.split())):
        print(i)
        sum += next(func, 0)
    return sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
