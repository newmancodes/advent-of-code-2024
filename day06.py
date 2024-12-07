from enum import Enum
from typing import Self
from typing import Tuple
from typing import Union


class EmptySpace:
    def __init__(self) -> None:
        self.__visited = False
        return None

    def get_visited(self) -> bool:
        return self.__visited

    def __set_visited(self, value: bool) -> None:
        self.__visited = value
        return None

    def visit(self) -> None:
        self.__set_visited(True)
        return None


class Obstruction:
    def __init__(self) -> None:
        return None


class Coordinate:
    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        return None

    def __add__(self, other: Self) -> Self:
        new_x = self.get_x() + other.get_x()
        new_y = self.get_y() + other.get_y()

        return Coordinate(new_x, new_y)

    def origin() -> Self:
        return Coordinate(0, 0)


class Orientation(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


class Guard:
    def get_location(self) -> Coordinate:
        return self.__location

    def set_location(self, value: Coordinate) -> None:
        self.__location = value
        return None

    def __get_orientation(self) -> Orientation:
        return self.__orientation

    def __set_orientation(self, value: Orientation) -> None:
        self.__orientation = value
        return None

    def __init__(self, location: Coordinate, orientation: Orientation) -> None:
        self.__location = location
        self.__orientation = orientation
        return None

    def get_next_location(self) -> Coordinate:
        match self.__get_orientation():
            case Orientation.NORTH:
                location_adjustment = Coordinate(0, -1)
            case Orientation.EAST:
                location_adjustment = Coordinate(1, 0)
            case Orientation.SOUTH:
                location_adjustment = Coordinate(0, 1)
            case Orientation.WEST:
                location_adjustment = Coordinate(-1, 0)

        return self.get_location() + location_adjustment

    def turn_clockwise(self) -> None:
        match self.__get_orientation():
            case Orientation.NORTH:
                new_orientation = Orientation.EAST
            case Orientation.EAST:
                new_orientation = Orientation.SOUTH
            case Orientation.SOUTH:
                new_orientation = Orientation.WEST
            case Orientation.WEST:
                new_orientation = Orientation.NORTH
        self.__set_orientation(new_orientation)


class Map:
    def __get_guard(self) -> Guard:
        return self.__guard

    def __get_map_height(self) -> int:
        return self.__map_height

    def __get_map_width(self) -> int:
        return self.__map_width

    def __get_tiles(self) -> list[list[Union[EmptySpace | Obstruction]]]:
        return self.__tiles

    def __get_tile(
        self, coordinate: Coordinate
    ) -> Union[EmptySpace | Obstruction | None]:
        if (
            coordinate.get_y() < 0
            or coordinate.get_y() >= self.__get_map_height()
            or coordinate.get_x() < 0
            or coordinate.get_x() >= self.__get_map_width()
        ):
            # Represents requesting an out of bounds tile
            return None

        return self.__get_tiles()[coordinate.get_y()][coordinate.get_x()]

    def __init__(
        self,
        tiles: list[list[EmptySpace | Obstruction]],
        guard: Guard,
    ) -> None:
        self.__tiles = tiles
        self.__map_height = len(tiles)
        # Assume all rows have the same width and there is at least one
        self.__map_width = len(tiles[0])
        self.__guard = guard
        # We have visited the guard's start location
        start_location = self.__get_tile(self.__get_guard().get_location())
        if type(start_location) is EmptySpace:
            start_location.visit()
        return None

    def walk_route(self) -> None:
        guard = self.__get_guard()

        while True:
            guards_next_location = guard.get_next_location()
            guards_next_tile = self.__get_tile(guards_next_location)
            match guards_next_tile:
                case EmptySpace():
                    guard.set_location(guards_next_location)
                    guards_next_tile.visit()
                case Obstruction():
                    guard.turn_clockwise()
                case None:
                    return None

    def count_visited_tiles(self) -> int:
        visited_tiles = list(
            filter(
                lambda t: type(t) is EmptySpace and t.get_visited(),
                [tile for rows in self.__get_tiles() for tile in rows],
            )
        )
        return len(visited_tiles)


class InputParser:
    def parse_file(filename: str) -> Map:
        lines = []

        with open(filename) as file:
            for line in file:
                lines.append(line)

        return InputParser.parse_input(lines)

    def parse_input(input: list[str]) -> Map:
        tiles = []
        for rowIndex, row in enumerate(input):
            rowTiles = []
            for characterIndex, character in enumerate(row):
                match character:
                    case "#":
                        tile = Obstruction()
                    case ".":
                        tile = EmptySpace()
                    case "^":
                        tile = EmptySpace()
                        guard = Guard(
                            Coordinate(characterIndex, rowIndex), Orientation.NORTH
                        )
                    case _:
                        continue

                rowTiles.append(tile)

            tiles.append(rowTiles)

        return Map(tiles, guard)


if __name__ == "__main__":
    map = InputParser.parse_file("./inputs/day06/first_input.txt")
    map.walk_route()
    print(f"Guard visiting {map.count_visited_tiles()} distinct tiles during his route")
