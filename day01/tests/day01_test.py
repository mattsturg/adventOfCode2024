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


# @pytest.fixture
# def real_list():
#     filename = "day01_in_1.txt"
#     return_list = []
#     with open(filename, 'r') as fileHandle:
#         for line in fileHandle:
#             return_list.append(line)
#     return return_list
#
#
# @pytest.fixture
# def test_list_2():
#     filename = "day01_in_2.txt"
#     return_list = []
#     with open(filename, 'r') as fileHandle:
#         for line in fileHandle:
#             return_list.append(line)
#     return return_list
#
#
# @pytest.fixture
# def real_list_2():
#     filename = "day01_in_3.txt"
#     return_list = []
#     with open(filename, 'r') as fileHandle:
#         for line in fileHandle:
#             return_list.append(line)
#     return return_list
#
#
# @pytest.fixture
# def real_list_dad():
#     filename = "day01_in_dad.txt"
#     return_list = []
#     with open(filename, 'r') as fileHandle:
#         for line in fileHandle:
#             return_list.append(line)
#     return return_list


def test_day01_mini(test_list):
    assert day01.calculate_calibration(test_list) == 142


# def test_day01_real(real_list):
#     assert day01.calculate_calibration(real_list) == 55488
#
#
# def test_day01_p2_mini(test_list_2):
#     assert day01.calculate_calibration_words(test_list_2) == 281
#
#
# def test_day01_p2_real(real_list_2):
#     assert day01.calculate_calibration_words(real_list_2) == 55614
#
#
# def test_day01_p2_dad(real_list_dad):
#     assert day01.calculate_calibration_words(real_list_dad) == 53866
