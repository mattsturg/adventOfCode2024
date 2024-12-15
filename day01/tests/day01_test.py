import pytest
import day01


@pytest.fixture
def test_list():
    filename = "day01_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list():
    filename = "day01_in_1.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def test_list_2():
    filename = "day01_in_0.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


@pytest.fixture
def real_list_2():
    filename = "day01_in_2.txt"
    return_list = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            return_list.append(line)
    return return_list


def test_day01_mini(test_list):
    assert day01.list_distance(test_list) == 11


def test_day01_real(real_list):
    assert day01.list_distance(real_list) == 1320851


def test_day01_p2_mini(test_list_2):
    assert day01.similarity_score(test_list_2) == 31


def test_day01_p2_real(real_list_2):
    assert day01.similarity_score(real_list_2) == 26859182
