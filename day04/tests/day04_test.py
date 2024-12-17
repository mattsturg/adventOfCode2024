import pytest
import day04


@pytest.fixture
def test_list():
    filename = "day04_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day04_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day04_mini(test_list):
    assert day04.xmas_search(test_list) == 18


def test_day04_real(real_list):
    assert day04.xmas_search(real_list) == 2521


def test_day04_p2_mini(test_list):
    assert day04.x_mas_search(test_list) == 9


def test_day04_real(real_list):
    assert day04.x_mas_search(real_list) == 1912
