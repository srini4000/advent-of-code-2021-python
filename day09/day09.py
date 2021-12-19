"""
--- Day 9: Smoke Basin ---
https://adventofcode.com/2021/day/9
"""
from dataclasses import dataclass
from typing import ClassVar
from collections.abc import Iterator
from collections import deque

LOCATION = tuple[int, int]


@dataclass
class HeightMap:
    grid: dict[LOCATION, int]
    width: ClassVar[int]
    height: ClassVar[int]

    @classmethod
    def from_string(cls, s: str):
        s = input_text
        grid = {
            (x, y): int(height)
            for y, line in enumerate(s.splitlines())
            for x, height in enumerate(line)
        }
        cls.height = len(s.splitlines())
        cls.width = len(s.splitlines()[0])

        return cls(grid)

    def in_bounds(self, id: LOCATION) -> bool:
        """Returns true if location id is in bounds"""
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, id: LOCATION) -> Iterator[LOCATION]:
        """Return list of neighbors locations"""
        (x, y) = id
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]  # R,L,U,D
        return (p for p in neighbors if self.in_bounds(p))

    def is_low_point(self, p: LOCATION) -> bool:
        return all(self.grid[neighbor] > self.grid[p] for neighbor in self.neighbors(p))

    def low_points(self) -> Iterator[LOCATION]:
        """Returns list of low points"""
        return (p for p in self.grid if self.is_low_point(p))

    def low_point_risk_levels(self) -> Iterator[int]:
        return (self.grid[p] + 1 for p in self.low_points())

    def get_basin_size(self, id: LOCATION) -> int:
        """Use BFS search to find basin_locations"""
        basin_locations: list[LOCATION] = []
        Q: deque[LOCATION] = deque()
        Q.append(id)
        visited: set[LOCATION] = set()
        while len(Q) != 0:
            p = Q.popleft()
            visited.add(p)
            neighbors = self.neighbors(p)
            basin_locations.append(p)
            for neighbor in neighbors:
                if neighbor not in visited and self.grid[neighbor] != 9:
                    visited.add(neighbor)
                    Q.append(neighbor)
        return len(basin_locations)


def part_1(input_text: str) -> int:
    height_map = HeightMap.from_string(input_text)
    return sum(risk_level for risk_level in height_map.low_point_risk_levels())


def part_2(input_text: str) -> int:
    height_map = HeightMap.from_string(input_text)
    basin_sizes = [height_map.get_basin_size(p) for p in height_map.low_points()]
    top3sizes = sorted(basin_sizes, reverse=True)[0:3]
    return top3sizes[0] * top3sizes[1] * top3sizes[2]


if __name__ == "__main__":
    input_text = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""
    assert part_1(input_text) == 15
    assert part_2(input_text) == 1134

    with open("day09/input.txt", "r") as file:
        input_text = file.read()

        part_1_answer = part_1(input_text)
        print(f"{part_1_answer = }")

        part_2_answer = part_2(input_text)
        print(f"{part_2_answer = }")
