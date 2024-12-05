import day05
import pytest
import sys


def test_middle_page_can_be_located():
    update = day05.Update([75, 47, 61, 53, 29])

    assert update.get_middle_page_number() == 61


def test_applicable_ordering_rule_is_detected():
    pages = [75, 47, 61, 53, 29]

    sut = day05.OrderingRule(47, 53)

    assert sut.is_applicable(pages) == True


def test_inapplicable_ordering_rule_is_detected_zero_matches():
    pages = [75, 47, 61, 53, 29]

    sut = day05.OrderingRule(32, 90)

    assert sut.is_applicable(pages) == False


def test_inapplicable_ordering_rule_is_detected_only_matches_first():
    pages = [75, 47, 61, 53, 29]

    sut = day05.OrderingRule(47, 90)

    assert sut.is_applicable(pages) == False


def test_inapplicable_ordering_rule_is_detected_only_matches_next():
    pages = [75, 47, 61, 53, 29]

    sut = day05.OrderingRule(32, 53)

    assert sut.is_applicable(pages) == False


def test_satisfied_ordering_rule_is_detected():
    pages = [75, 47, 61, 53, 29]

    sut = day05.OrderingRule(47, 53)

    assert sut.is_satisfied(pages) == True


def test_unsatisfied_ordering_rule_is_detected():
    pages = [75, 47, 61, 53, 29]

    sut = day05.OrderingRule(53, 47)

    assert sut.is_satisfied(pages) == False


def test_printable_update_is_detected():
    ordering_rules = [
        day05.OrderingRule(47, 53),
        day05.OrderingRule(97, 13),
        day05.OrderingRule(97, 61),
        day05.OrderingRule(97, 47),
        day05.OrderingRule(75, 29),
        day05.OrderingRule(61, 13),
        day05.OrderingRule(75, 53),
        day05.OrderingRule(29, 13),
        day05.OrderingRule(97, 29),
        day05.OrderingRule(53, 29),
        day05.OrderingRule(61, 53),
        day05.OrderingRule(97, 53),
        day05.OrderingRule(61, 29),
        day05.OrderingRule(47, 13),
        day05.OrderingRule(75, 47),
        day05.OrderingRule(97, 75),
        day05.OrderingRule(47, 61),
        day05.OrderingRule(75, 61),
        day05.OrderingRule(47, 29),
        day05.OrderingRule(75, 13),
        day05.OrderingRule(53, 13),
    ]
    sut = day05.Update([75, 47, 61, 53, 29])

    assert sut.should_be_printed(ordering_rules) == True


def test_initial_example_has_a_total_of_143():
    input = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
        "",
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47",
    ]

    sut = day05.InputParser.parse_input(input)

    assert sut.sum_middle_page_of_printed_update() == 143


def test_initial_example_with_reordering_has_a_total_of_123():
    input = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
        "",
        "75,47,61,53,29",
        "97,61,53,29,13",
        "75,29,13",
        "75,97,47,61,53",
        "61,13,29",
        "97,13,75,29,47",
    ]

    sut = day05.InputParser.parse_input(input)

    assert sut.sum_middle_page_of_reordered_printed_update() == 123


if __name__ == "__main__":
    sys.exit(pytest.main(["./test_day05.py"]))
