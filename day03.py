import re


class Operation:
    def __init__(self, operation: str, x: int, y: int):
        self.operation = operation
        self.x = x
        self.y = y

    def execute(self) -> int:
        match self.operation:
            case "mul":
                return self.x * self.y


class SectionParser:
    def parse(section: str) -> list[Operation]:
        pattern = re.compile(r"(.*?(?P<operation>mul)\((?P<x>\d+),(?P<y>\d+)\))+?")
        position = 0
        operations = []

        while match := pattern.search(section, position):
            position += match.end() - match.start()
            operation = Operation(
                match.group("operation"), int(match.group("x")), int(match.group("y"))
            )
            operations.append(operation)

        return operations


class Calculator:
    def calculate_for_section(section: str) -> int:
        operations = SectionParser.parse(section)
        return Calculator.calculate(operations)

    def calculate(operations: list[Operation]) -> int:
        result = 0
        for operation in operations:
            result += operation.execute()
        return result


class InputParser:
    def parse_file(filename: str) -> list[Operation]:
        operations = []

        with open(filename) as file:
            for line in file:
                operations = operations + SectionParser.parse(line)

        return operations


if __name__ == "__main__":
    operations = InputParser.parse_file("./inputs/day03/first_input.txt")
    result = Calculator.calculate(operations)
    print(f"Result is {result}")
