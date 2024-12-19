import pytest
import day05


@pytest.fixture
def test_list():
    filename = "day05_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day05_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day05_mini(test_list):
    assert day05.update_ordering(test_list) == 143


def test_day05_real(real_list):
    assert day05.update_ordering(real_list) == 7024


def test_day05_p2_mini(test_list):
    assert day05.update_fixing(test_list) == 123


def test_day05_real(real_list):
    assert day05.update_fixing(real_list) == 4151
