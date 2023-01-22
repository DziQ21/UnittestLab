import pytest
from main import bubble_sort

def test_sort_with_three_elements():
    arr = [3, 2, 1]
    sorted_arr = [1, 2, 3]
    assert bubble_sort(arr) == sorted_arr

def test_sort_with_five_elements():
    arr = [5, 1, 4, 2, 8]
    sorted_arr = [1, 2, 4, 5, 8]
    assert bubble_sort(arr) == sorted_arr

def test_sort_with_repeated_elements():
    arr = [5, 5, 5, 5]
    sorted_arr = [5, 5, 5, 5]
    assert bubble_sort(arr) == sorted_arr

def test_sort_with_empty_array():
    arr = []
    sorted_arr = []
    assert bubble_sort(arr) == sorted_arr


@pytest.mark.parametrize("test_input,expected", [
    ([4], [4]),
    ([1], [1]),
    ([0], [0]),
    ([3], [3]),
])
def test_bubble_sort_with_1_lenght_table(test_input, expected):
    result = bubble_sort(test_input)
    assert result == expected