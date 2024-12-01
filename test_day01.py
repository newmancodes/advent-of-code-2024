import day01
import pytest
import sys


def test_example_input_can_be_parsed():
    left_list, right_list = day01.InputParser.parse_file(
        "./inputs/day01/example_input.txt"
    )

    assert left_list == [3, 4, 2, 1, 3, 3]
    assert right_list == [4, 3, 5, 3, 9, 3]


def test_initial_example_has_a_distance_of_11():
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]

    assert day01.ListComparer.calculate_distance(left_list, right_list) == 11


if __name__ == "__main__":
    sys.exit(pytest.main(["./test_day01.py"]))
