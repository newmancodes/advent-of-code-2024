class ListComparer:
    def calculate_distance(x: list[int], y: list[int]) -> int:
        x.sort()
        y.sort()

        total_distance = 0

        for index, x_item in enumerate(x):  # Assumes x and y have the same length
            position_distance = abs(x_item - y[index])
            total_distance = total_distance + position_distance

        return total_distance

    def calculate_similarity(x: list[int], y: list[int]) -> int:
        y_occurance_counts = {}
        for y_item in y:
            seen_so_far = y_occurance_counts.get(y_item, 0)
            seen_so_far += 1
            y_occurance_counts.update({y_item: seen_so_far})

        similarity = 0

        for x_item in x:
            similarity += x_item * y_occurance_counts.get(x_item, 0)

        return similarity


class InputParser:
    def parse_file(filename: str) -> tuple[list[int], list[int]]:
        left_list = []
        right_list = []

        with open(filename) as file:
            for line in file:
                numbers = line.split("   ")
                left_list.append(int(numbers[0]))
                right_list.append(int(numbers[1]))

        return (left_list, right_list)


if __name__ == "__main__":
    first_input_filename = "./inputs/day01/first_input.txt"
    left_list, right_list = InputParser.parse_file(first_input_filename)
    distance = ListComparer.calculate_distance(left_list, right_list)
    print(f"Distance between the lists in {first_input_filename} is {distance}")

    similarity = ListComparer.calculate_similarity(left_list, right_list)
    print(f"Similarity of the lists in {first_input_filename} is {similarity}")
