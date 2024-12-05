import math
from typing import Self
from typing import Tuple


class OrderingRule:
    def __init__(self, first: int, next: int):
        self.__first = first
        self.__next = next

    def get_first(self) -> int:
        return self.__first

    def get_next(self) -> int:
        return self.__next

    def is_applicable(self, pages: list[int]) -> bool:
        return self.get_first() in pages and self.get_next() in pages

    def is_satisfied(self, pages: list[int]) -> bool:
        first = self.get_first()
        next = self.get_next()

        location_of_first = [
            index for index, value in enumerate(pages) if value == first
        ]
        location_of_next = [index for index, value in enumerate(pages) if value == next]

        return location_of_first < location_of_next


class Update:
    def __init__(self, updated_pages: list[int]):
        self.__updated_pages = updated_pages

    def __check_applicable(self, ordering_rule: OrderingRule) -> bool:
        return ordering_rule.is_applicable(self.get_updated_pages())

    def __check_satisfied(self, ordering_rule: OrderingRule) -> bool:
        return ordering_rule.is_satisfied(self.get_updated_pages())

    def get_updated_pages(self) -> list[int]:
        return self.__updated_pages

    def should_be_printed(self, ordering_rules: list[OrderingRule]) -> bool:
        applicable_rules = list(filter(self.__check_applicable, ordering_rules))
        satisfied_rules = list(filter(self.__check_satisfied, applicable_rules))

        for applicable_rule in applicable_rules:
            if not applicable_rule in satisfied_rules:
                return False

        return True

    def reorder_to_satisfy(self, ordering_rules: list[OrderingRule]) -> Self:
        # TODO : Reorder the updated pages such that the applicable ordering rules are satisfied
        return self

    def get_middle_page_number(self) -> int:
        updated_pages = self.get_updated_pages()
        return self.get_updated_pages()[math.trunc(len(updated_pages) / 2)]


class Instruction:
    def __init__(self, ordering_rules: list[OrderingRule], updated: list[Update]):
        self.__ordering_rules = ordering_rules
        self.__updated = updated

    def get_ordering_rules(self) -> list[OrderingRule]:
        return self.__ordering_rules

    def get_updated(self) -> list[Update]:
        return self.__updated

    def __should_be_printed(self, update: Update) -> bool:
        return update.should_be_printed(self.get_ordering_rules())

    def __should_not_be_printed(self, update: Update) -> bool:
        return not update.should_be_printed(self.get_ordering_rules())

    def __reorder_to_satisfy(self, update: Update) -> Self:
        return update.reorder_to_satisfy(self.get_ordering_rules())

    def sum_middle_page_of_printed_update(self) -> int:
        return sum(
            update.get_middle_page_number()
            for update in list(filter(self.__should_be_printed, self.get_updated()))
        )

    def sum_middle_page_of_reordered_printed_update(self) -> int:
        return sum(
            update.get_middle_page_number()
            for update in list(
                map(
                    lambda update: self.__reorder_to_satisfy(update),
                    list(filter(self.__should_not_be_printed, self.get_updated())),
                )
            )
        )


class InputParser:
    def parse_file(filename: str) -> Instruction:
        lines = []

        with open(filename) as file:
            for line in file:
                lines.append(line)

        return InputParser.parse_input(lines)

    def parse_input(input: list[str]) -> Instruction:
        am_parsing_ordering_rules = True
        am_parsing_updates = False

        ordering_rules = []
        updated = []

        for line in input:
            if line == "" or line == "\n":
                am_parsing_ordering_rules = False
                am_parsing_updates = True
                continue
            elif am_parsing_ordering_rules == True:
                rule_components = line.split("|")
                ordering_rules.append(
                    OrderingRule(int(rule_components[0]), int(rule_components[1]))
                )
            elif am_parsing_updates == True:
                updated.append(Update(list(map(int, line.split(",")))))

        return Instruction(ordering_rules, updated)


if __name__ == "__main__":
    instruction = InputParser.parse_file("./inputs/day05/first_input.txt")
    sum_of_middle_pages = instruction.sum_middle_page_of_printed_update()
    print(f"Calculated that the middle pages sum to {sum_of_middle_pages}")
