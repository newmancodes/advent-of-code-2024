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


if __name__ == "__main__":
    print("Hello, World!")
