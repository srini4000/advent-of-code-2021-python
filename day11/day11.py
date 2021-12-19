"""
--- Day 11: Dumbo Octopus ---
https://adventofcode.com/2021/day/11
"""
from collections import deque
from dataclasses import dataclass
from typing import ClassVar, Iterator

LOCATION = tuple[int, int]
GRID = dict[LOCATION, int]


@dataclass
class Grid:
    grid: GRID
    steps: int = 0
    flash_count: int = 0
    width: ClassVar[int]
    height: ClassVar[int]

    @classmethod
    def from_string(cls, s: str):
        """Returns Grid object constructed from given string"""
        # s = input_text
        lines = s.splitlines()
        grid: GRID = {
            (x, y): int(num)
            for y, line in enumerate(lines)
            for x, num in enumerate(line)
        }
        cls.height = len(lines)
        cls.width = len(lines[0])
        return cls(grid)

    def __repr__(self) -> str:
        s = ""
        for y in range(self.height):
            for x in range(self.width):
                s += str(self.grid[(x, y)])
            s += "\n"
        return s

    def in_bounds(self, id: LOCATION) -> bool:
        """Returns true if location id is in bounds"""
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors_4(self, id: LOCATION) -> Iterator[LOCATION]:
        """
        Yields row,column tuples of neighbors.
        Only Left, Right, Up, Down neighbors are considered
        Diagonal neighbors are not considered
        """
        (x, y) = id
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]  # L,R,U,D
        return (p for p in neighbors if self.in_bounds(p))

    def neighbors_8(self, id: LOCATION) -> Iterator[LOCATION]:
        """
        Yields row,column tuples of neighbors.
        Diagonal neighbors are considered
        """
        (x, y) = id
        neighbors = [
            (x - 1, y),  # West
            (x + 1, y),  # East
            (x, y - 1),  # North
            (x, y + 1),  # South
            (x - 1, y - 1),  # NorthWest
            (x - 1, y + 1),  # SouthWest
            (x + 1, y - 1),  # NorthEast
            (x + 1, y + 1),  # SouthEast
        ]
        return (p for p in neighbors if self.in_bounds(p))

    def add_steps(self, n: int):
        for _ in range(n):
            self.add_step()

    def add_step(self) -> int:
        """Returns how many flashes in this step"""
        Q: deque[tuple[int, int]] = deque()
        for (x, y) in self.grid:
            self.grid[(x, y)] += 1
            if self.grid[(x, y)] >= 10:
                self.grid[(x, y)] = 0
                Q.append((x, y))
        step_flash_count = 0  # count how many flashes in this step
        while len(Q) > 0:
            location = Q.pop()
            self.flash_count += 1
            step_flash_count += 1
            for neighbor in self.neighbors_8(location):
                if self.grid[neighbor] != 0:
                    # ignore flashed neighbors in this step
                    self.grid[neighbor] += 1
                    if self.grid[neighbor] == 10:
                        self.grid[neighbor] = 0
                        Q.append(neighbor)
        self.steps += 1
        return step_flash_count


def part_1(input_text: str) -> int:
    g = Grid.from_string(input_text)
    g.add_steps(100)
    return g.flash_count


def part_2(input_text: str) -> int:
    g = Grid.from_string(input_text)
    steps = 1
    while g.add_step() != 100:
        steps += 1
    return steps


if __name__ == "__main__":
    input_text = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

    assert part_1(input_text) == 1656
    assert part_2(input_text) == 195

    with open("day11/input.txt", "r") as file:
        input_text = file.read()

        part_1_answer = part_1(input_text)
        print(f"{part_1_answer = }")

        part_2_answer = part_2(input_text)
        print(f"{part_2_answer = }")
