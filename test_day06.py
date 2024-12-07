import day06
import pytest
import sys


def test_initial_example_has_a_position_visitation_of_41():
    input = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]

    sut = day06.InputParser.parse_input(input)
    sut.walk_route()

    assert sut.count_visited_tiles() == 41


if __name__ == "__main__":
    sys.exit(pytest.main(["./test_day06.py"]))
