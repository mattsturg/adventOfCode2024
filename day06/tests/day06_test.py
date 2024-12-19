import pytest
import day06


@pytest.fixture
def test_list():
    filename = "day06_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day06_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day06_mini(test_list):
    assert day06.guard_path(test_list) == 41


def test_day06_real(real_list):
    assert day06.guard_path(real_list) == 5086


def test_day05_p2_mini(test_list):
    assert day06.guard_path2(test_list) == 6


def test_day06_p2_real(real_list):
    assert day06.guard_path2(real_list) == 6
