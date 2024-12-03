import day03
import pytest
import sys


def test_initial_example_has_a_result_of_161():
    section = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    assert day03.Calculator.calculate_for_section(section) == 161


@pytest.mark.skip(reason="this is part two")
def test_example_with_do_and_dont_has_a_result_of_48():
    section = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    assert day03.Calculator.calculate_for_section(section) == 48


if __name__ == "__main__":
    sys.exit(pytest.main(["./test_day03.py"]))
