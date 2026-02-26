# src/basics.py

def sum_two_numbers(a: int, b: int) -> int:
    """Возвращает сумму двух чисел"""
    return a + b


def is_even(number: int) -> bool:
    """Проверяет, является ли число чётным"""
    return number % 2 == 0


def get_grade(score: int) -> str:
    """Возвращает оценку по баллам (0-100)"""
    if score < 0 or score > 100:
        return "Некорректный балл"
    elif score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"