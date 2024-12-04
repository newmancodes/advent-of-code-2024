import day04
import pytest
import sys


def test_initial_example_has_a_result_of_18():
    puzzle = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]

    sut = day04.WordSearch(puzzle)

    assert sut.search_for("XMAS") == 18


if __name__ == "__main__":
    sys.exit(pytest.main(["./test_day04.py"]))
