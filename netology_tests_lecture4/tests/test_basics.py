# tests/test_basics.py
import pytest
import sys
import os

# Добавляем папку src в путь, чтобы импортировать функции
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from basics import sum_two_numbers, is_even, get_grade


class TestSumTwoNumbers:
    """Тесты для функции sum_two_numbers"""
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (100, 200, 300),
        (-5, -10, -15),
    ])
    def test_sum_positive_negative_zero(self, a, b, expected):
        assert sum_two_numbers(a, b) == expected


class TestIsEven:
    """Тесты для функции is_even"""
    
    @pytest.mark.parametrize("number,expected", [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-7, False),
        (100, True),
    ])
    def test_is_even_various_numbers(self, number, expected):
        assert is_even(number) == expected


class TestGetGrade:
    """Тесты для функции get_grade"""
    
    @pytest.mark.parametrize("score,expected", [
        (95, "A"),
        (80, "B"),
        (65, "C"),
        (50, "D"),
        (30, "F"),
        (101, "Некорректный балл"),
        (-10, "Некорректный балл"),
        (90, "A"),  # граница
        (75, "B"),  # граница
        (60, "C"),  # граница
        (45, "D"),  # граница
    ])
    def test_get_grade_all_cases(self, score, expected):
        assert get_grade(score) == expected