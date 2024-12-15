import pytest
import day02


@pytest.fixture
def test_list():
    filename = "day02_in.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture()
def real_list():
    filename = "day02_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day02_mini(test_list):
    assert day02.count_safe_lines(test_list) == 2


def test_day02_real(real_list):
    assert day02.count_safe_lines(real_list) == 686


def test_day02_p2_mini(test_list):
    assert day02.count_safe_lines_tolerator(test_list) == 4


def test_day02_p2_real(real_list):
    assert day02.count_safe_lines_tolerator(real_list) == 717


def test_day02_p2_real_brute(real_list):
    assert day02.brute_force(real_list) == 717
