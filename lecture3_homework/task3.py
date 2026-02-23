from datetime import datetime
from typing import Callable, Any, Union


# --- Декоратор logger из Задания 2 ---
def logger(path: str) -> Callable:
    """Декоратор, который записывает логи в указанный файл"""

    def __logger(old_function: Callable) -> Callable:
        def new_function(*args: Any, **kwargs: Any) -> Any:
            result = old_function(*args, **kwargs)

            with open(path, "a", encoding="utf-8") as f:
                f.write(
                    f"{datetime.now()} - Вызов функции: {old_function.__name__}, "
                    f"Аргументы: {args}, {kwargs}, Результат: {result}\n"
                )

            return result

        return new_function

    return __logger


# --- Код из netology_lesson2 с применённым логгером ---


@logger("lesson2_log.log")
def flat_generator(list_of_lists):
    """Генератор для плоского списка"""
    for sub_list in list_of_lists:
        for item in sub_list:
            yield item


@logger("lesson2_log.log")
def process_list(data):
    """Обрабатывает список и возвращает результат"""
    result = []
    for item in data:
        result.append(item)
    return result


@logger("lesson2_log.log")
def count_items(list_of_lists):
    """Считает количество элементов"""
    count = 0
    for sub_list in list_of_lists:
        count += len(sub_list)
    return count


# --- Тестирование ---
if __name__ == "__main__":
    print("Запуск приложения с логгером...")

    list_of_lists = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    # Тест 1: генератор
    result1 = list(flat_generator(list_of_lists))
    print(f"Генератор: {result1}")

    # Тест 2: обработка списка
    result2 = process_list(result1)
    print(f"Обработка: {len(result2)} элементов")

    # Тест 3: подсчёт
    result3 = count_items(list_of_lists)
    print(f"Всего элементов: {result3}")

    print("\nГотово! Проверь файл lesson2_log.log")
