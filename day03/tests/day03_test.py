import pytest
import day03


@pytest.fixture
def test_list():
    filename = "day03_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day03_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def test_list_2():
    filename = "day03_in_2.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list_2():
    filename = "day03_in_3.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day03_mini(test_list):
    assert day03.corrupt_mem(test_list) == 161


def test_day03_real(real_list):
    assert day03.corrupt_mem(real_list) == 0


def test_day03_p2_mini(test_list_2):
    assert day03.corrupt_mem_p2(test_list_2) == 48


def test_day03_real(real_list_2):
    assert day03.corrupt_mem_p2(real_list_2) == 59097164
