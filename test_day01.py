import day01
import pytest
import sys

def test_greeting_is_hello():
    puzzle = day01.Day01Puzzle()
    assert puzzle.greeting() == "hello"

if __name__ == "__main__":
    sys.exit(pytest.main(["./test_day01.py"]))