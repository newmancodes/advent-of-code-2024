from typing import Tuple


class WordSearch:
    def __init__(self, puzzle: list[str]):
        self.puzzle = puzzle
        self.puzzle_width = len(puzzle[0])
        self.puzzle_height = len(puzzle)

    def __matches_word(
        self,
        word: str,
        first_character_at: Tuple[int, int],
        look_iteration: Tuple[int, int],
    ) -> bool:
        previous_character_at = first_character_at

        for char in word[1:]:
            look_at = (
                previous_character_at[0] + look_iteration[0],
                previous_character_at[1] + look_iteration[1],
            )

            if look_at[0] < 0 or look_at[0] >= self.puzzle_width:
                # Out of bounds (width)
                return False
            elif look_at[1] < 0 or look_at[1] >= self.puzzle_height:
                # Out of bounds (height)
                return False
            elif self.puzzle[look_at[1]][look_at[0]] == char:
                previous_character_at = look_at
                continue
            else:
                return False

        return True

    def search_for(self, word: str) -> int:
        first_character = word[0]
        found_count = 0

        look_east = (1, 0)
        look_south_east = (1, 1)
        look_south = (0, 1)
        look_south_west = (-1, 1)
        look_west = (-1, 0)
        look_north_west = (-1, -1)
        look_north = (0, -1)
        look_north_east = (1, -1)

        step_collections = [
            look_east,
            look_south_east,
            look_south,
            look_south_west,
            look_west,
            look_north_west,
            look_north,
            look_north_east,
        ]

        for line_index, line in enumerate(self.puzzle):
            for char_index, char in enumerate(line):
                if char == first_character:
                    for step_collection in step_collections:
                        if self.__matches_word(
                            word, (char_index, line_index), step_collection
                        ):
                            found_count += 1

        return found_count

    def search_for_interlocked(self, word: str) -> int:
        central_character = word[1]  # Assumes word length of three
        found_count = 0

        for line_index, line in enumerate(self.puzzle):
            for char_index, char in enumerate(line):
                if line_index == 0 or line_index == self.puzzle_height - 1:
                    # Out of bounds (height)
                    continue
                elif char_index == 0 or char_index == self.puzzle_width - 1:
                    # Out of bounds (width)
                    continue
                elif char == central_character:
                    top_left = (char_index - 1, line_index - 1)
                    top_right = (char_index + 1, line_index - 1)
                    bottom_left = (char_index - 1, line_index + 1)
                    bottom_right = (char_index + 1, line_index + 1)

                    top_left_character = self.puzzle[top_left[1]][top_left[0]]
                    top_right_character = self.puzzle[top_right[1]][top_right[0]]
                    bottom_left_character = self.puzzle[bottom_left[1]][bottom_left[0]]
                    bottom_right_character = self.puzzle[bottom_right[1]][
                        bottom_right[0]
                    ]

                    if (
                        (
                            top_left_character == word[0]
                            and bottom_right_character == word[2]
                        )
                        or (
                            top_left_character == word[2]
                            and bottom_right_character == word[0]
                        )
                    ) and (
                        (
                            top_right_character == word[0]
                            and bottom_left_character == word[2]
                        )
                        or (
                            top_right_character == word[2]
                            and bottom_left_character == word[0]
                        )
                    ):
                        found_count += 1

        return found_count


class InputParser:
    def parse_file(filename: str) -> list[str]:
        lines = []

        with open(filename) as file:
            for line in file:
                lines.append(line)

        return lines


if __name__ == "__main__":
    puzzle = InputParser.parse_file("./inputs/day04/first_input.txt")
    word_search = WordSearch(puzzle)
    match_count = word_search.search_for("XMAS")
    print(f"Found {match_count} instances of XMAS")
    match_count = word_search.search_for_interlocked("MAS")
    print(f"Found {match_count} instances of interlocked MAS")
