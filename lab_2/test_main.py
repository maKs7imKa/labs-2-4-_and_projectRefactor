import pytest
from main import correlation1, auto_cor, cor, plot1

# Тест кореляції
def test_correlation1_basic():
    a = [1, 2, 3, 4]
    b = [4, 3, 2, 1]
    N = 4
    result = correlation1(a, b, N)
    expected = [30, 24, 22, 24]  # Очікуване значення для даного прикладу
    assert result == expected

# Тест для auto_correlation
def test_auto_cor_basic():
    a = [1, 2, 3, 4]
    result = auto_cor(a)
    expected = [30, 24, 22, 24]  # Очікуване значення для auto_cor
    assert result == expected

# Тест для cross_correlation
def test_cor_basic():
    a = [1, 2, 3]
    b = [4, 5, 6]
    result = cor(a, b)
    expected = [32, 29, 29]  # Очікуване значення для cor
    assert result == expected

# Тест на випадок порожніх списків для auto_correlation
def test_auto_cor_empty_input():
    a = []
    result = auto_cor(a)
    assert result == []  # Очікуємо порожній список

# Тест на випадок списків з одним елементом
def test_auto_cor_single_element():
    a = [5]
    result = auto_cor(a)
    assert result == [25]  # Оскільки a = [5], то результат буде 5*5 = 25

# Тест для додавання нулів до Y в cor
def test_cor_padding_zeros():
    a = [1, 2, 3]
    b = [4, 5]
    result = cor(a, b)
    expected = [32, 29, 29]  # Очікувані значення
    assert result == expected

# Тест для значень з негативними числами
def test_auto_cor_with_negative_values():
    a = [-1, -2, -3, -4]
    result = auto_cor(a)
    expected = [30, 24, 22, 24]  # Очікуване значення для цього списку
    assert result == expected

# Тест для кореляції з нулями
def test_cor_with_zeros():
    a = [0, 2, 3]
    b = [0, 0, 0]
    result = cor(a, b)
    expected = [0, 0, 0]  # Очікуємо, що результат буде нульовим
    assert result == expected

# Тест для великих чисел
def test_cor_with_large_numbers():
    a = [100000, 200000, 300000]
    b = [400000, 500000, 600000]
    result = cor(a, b)
    expected = [320000000000, 290000000000, 290000000000]  # Очікувані значення
    assert result == expected

# Тест для автоматичної кореляції з великими входами
def test_auto_cor_large_input():
    a = [i for i in range(1000)]
    result = auto_cor(a)
    assert len(result) == 1000  # Перевіряємо, чи правильний розмір списку після кореляції

# Тест для plot1, щоб переконатися, що функція працює без помилок
def test_plot1():
    try:
        plot1([1, 2, 3])
    except Exception:
        pytest.fail("plot1 викликає помилку")
