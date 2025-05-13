import pytest
from main_ref_v2 import Correlation

def test_auto_correlation_basic():
    a = [1, 2, 3, 4]
    corr = Correlation(a)
    result = corr.auto_correlation(len(a))
    expected = [30, 24, 22, 24]  #
    assert result == expected

def test_cross_correlation_basic():
    a = [1, 2, 3]
    b = [4, 5, 6]
    corr = Correlation(a, b)
    result = corr.cross_correlation(len(a))
    expected = [32, 29, 29]
    assert result == expected

def test_padding_y_for_cross_correlation():
    a = [1, 2, 3]
    b = [4, 5]
    corr = Correlation(a, b)
    corr.cross_correlation(len(a))
    assert len(corr.b) == len(a)

def test_empty_input():
    a = []
    corr = Correlation(a)
    result = corr.auto_correlation(len(a))
    assert result == []

def test_single_element_input():
    a = [1]
    corr = Correlation(a)
    result = corr.auto_correlation(len(a))
    assert result == [1]

def test_cross_correlation_different_length():
    a = [1, 2, 3]
    b = [4, 5]
    corr = Correlation(a, b)
    result = corr.cross_correlation(len(a))
    expected = [14, 23, 17]
    assert result == expected

def test_auto_correlation_with_negative_values():
    a = [-1, -2, -3, -4]
    corr = Correlation(a)
    result = corr.auto_correlation(len(a))
    expected = [30, 24, 22, 24]
    assert result == expected

def test_cross_correlation_with_zeros():
    a = [0, 2, 3]
    b = [0, 0, 0]
    corr = Correlation(a, b)
    result = corr.cross_correlation(len(a))
    expected = [0, 0, 0]
    assert result == expected

def test_cross_correlation_with_large_numbers():
    a = [100000, 200000, 300000]
    b = [400000, 500000, 600000]
    corr = Correlation(a, b)
    result = corr.cross_correlation(len(a))
    expected = [320000000000, 290000000000, 290000000000]
    assert result == expected

def test_auto_correlation_with_large_input():
    a = [i for i in range(1000)]
    corr = Correlation(a)
    result = corr.auto_correlation(len(a))
    assert len(result) == 1000


 #  python -m pytest -v test_ref_v.py --disable-warnings

 # python -m pylint test_main.py