import day02
import pytest
import sys


def test_example_input_can_be_parsed():
    reports = day02.InputParser.parse_file("./inputs/day02/example_input.txt")

    assert len(reports) == 6
    assert reports[0].levels == [7, 6, 4, 2, 1]
    assert reports[1].levels == [1, 2, 7, 8, 9]
    assert reports[2].levels == [9, 7, 6, 2, 1]
    assert reports[3].levels == [1, 3, 2, 4, 5]
    assert reports[4].levels == [8, 6, 4, 4, 1]
    assert reports[5].levels == [1, 3, 6, 7, 9]


def test_initial_example_first_level_is_safe():
    report = day02.Report([7, 6, 4, 2, 1])

    assert report.is_safe() == True


def test_initial_example_second_level_is_unsafe():
    report = day02.Report([1, 2, 7, 8, 9])

    assert report.is_safe() == False


def test_initial_example_fifth_level_is_unsafe():
    report = day02.Report([8, 6, 4, 4, 1])

    assert report.is_safe() == False


def test_initial_example_forth_level_is_safe_when_the_problem_dampener():
    report = day02.Report([1, 3, 2, 4, 5])

    assert report.is_safe(True) == True


def test_initial_example_fifth_level_is_safe_when_the_problem_dampener():
    report = day02.Report([8, 6, 4, 4, 1])

    assert report.is_safe(True) == True


def test_initial_example_has_2_safe_reports():
    reports = [
        day02.Report([7, 6, 4, 2, 1]),
        day02.Report([1, 2, 7, 8, 9]),
        day02.Report([9, 7, 6, 2, 1]),
        day02.Report([1, 3, 2, 4, 5]),
        day02.Report([8, 6, 4, 4, 1]),
        day02.Report([1, 3, 6, 7, 9]),
    ]

    assert day02.Report.count_safe(reports) == 2


def test_initial_example_has_4_safe_reports_when_applying_the_problem_dampener():
    reports = [
        day02.Report([7, 6, 4, 2, 1]),
        day02.Report([1, 2, 7, 8, 9]),
        day02.Report([9, 7, 6, 2, 1]),
        day02.Report([1, 3, 2, 4, 5]),
        day02.Report([8, 6, 4, 4, 1]),
        day02.Report([1, 3, 6, 7, 9]),
    ]

    assert day02.Report.count_safe(reports, True) == 4


if __name__ == "__main__":
    sys.exit(pytest.main(["./test_day02.py"]))
