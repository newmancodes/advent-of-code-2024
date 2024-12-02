class Report:
    def count_safe(reports: list, apply_problem_dampener: bool = False) -> int:
        safe_reports = 0

        for report in reports:
            if report.is_safe(apply_problem_dampener):
                safe_reports += 1

        return safe_reports

    def __init__(self, levels: list[int] = []):
        self.levels = levels

    def is_safe(self, apply_problem_dampener: bool = False) -> bool:
        max_level_difference = 0
        detected_increase = False
        detected_decrease = False
        detected_static = False
        previous_level = self.levels[0]

        for index in range(1, len(self.levels)):
            current_level = self.levels[index]

            if current_level > previous_level:
                detected_increase = True
            elif current_level < previous_level:
                detected_decrease = True
            else:
                detected_static = True

            difference = abs(current_level - previous_level)
            if difference > max_level_difference:
                max_level_difference = difference

            previous_level = current_level

        is_safe = (
            not detected_static
            and detected_decrease != detected_increase
            and max_level_difference <= 3
        )

        if not is_safe and apply_problem_dampener:
            for index in range(0, len(self.levels)):
                report_missing_level_at_index = Report(
                    [level for i, level in enumerate(self.levels) if i != index]
                )
                if report_missing_level_at_index.is_safe():
                    return True

        return is_safe


class InputParser:
    def parse_file(filename: str) -> list[Report]:
        reports = []

        with open(filename) as file:
            for line in file:
                levels = line.split(" ")
                levels_as_numbers = list(map(int, levels))
                report = Report(levels_as_numbers)
                reports.append(report)

        return reports


if __name__ == "__main__":
    first_input_filename = "./inputs/day02/first_input.txt"
    reports = InputParser.parse_file(first_input_filename)
    safe_report_count = Report.count_safe(reports)
    print(f"There are {safe_report_count} safe reports in the input")
    safe_report_count_when_applying_problem_dampener = Report.count_safe(reports, True)
    print(
        f"When applying the problem dampener, there are {safe_report_count_when_applying_problem_dampener} safe reports in the input"
    )
