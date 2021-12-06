"""
Hydrothermal Venture
https://adventofcode.com/2021/day/5
"""
from dataclasses import dataclass
from collections import Counter


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    @classmethod
    def from_string(cls, s: str):
        x_str, y_str = s.split(",")
        return cls(x=int(x_str), y=int(y_str))


@dataclass(frozen=True)
class Line:
    start: Point
    end: Point

    @classmethod
    def from_string(cls, s: str):
        """Line.from_string('0,9 -> 5,9')"""
        start_xy_str, end_xy_str = s.split(" -> ")
        return cls(
            start=Point.from_string(start_xy_str), end=Point.from_string(end_xy_str)
        )

    @property
    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    @property
    def is_veritical(self) -> bool:
        return self.start.x == self.end.x

    @property
    def is_diagonal(self) -> bool:
        return abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y)

    @property
    def all_points(self) -> list[Point]:
        ret: list[Point] = []
        if self.is_horizontal:
            step = -1 if self.end.x < self.start.x else 1
            ret = [
                Point(x=i, y=self.start.y)
                for i in range(self.start.x, self.end.x + step, step)
            ]
        elif self.is_veritical:
            step = -1 if self.end.y < self.start.y else 1
            ret = [
                Point(x=self.start.x, y=j)
                for j in range(self.start.y, self.end.y + step, step)
            ]
        elif self.is_diagonal:
            x_step = 1 if self.start.x < self.end.x else -1
            y_step = 1 if self.start.y < self.end.y else -1

            x_nums = [x for x in range(self.start.x, self.end.x + x_step, x_step)]
            y_nums = [y for y in range(self.start.y, self.end.y + y_step, y_step)]
            ret = [Point(x, y) for x, y in zip(x_nums, y_nums)]

        return ret


def get_data(input_text: str) -> list[Line]:
    """
    returns list of Line objects
    """
    lines = [Line.from_string(line_str) for line_str in input_text.splitlines()]
    return lines


def part_1(lines: list[Line]) -> int:
    filtered_lines = [line for line in lines if line.is_horizontal or line.is_veritical]
    points = [point for line in filtered_lines for point in line.all_points]
    return sum(1 for v in Counter(points).values() if v >= 2)


def part_2(lines: list[Line]) -> int:
    filtered_lines = [
        line
        for line in lines
        if line.is_horizontal or line.is_veritical or line.is_diagonal
    ]
    points = [point for line in filtered_lines for point in line.all_points]
    return sum(1 for v in Counter(points).values() if v >= 2)


if __name__ == "__main__":
    input_text = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

    lines = get_data(input_text)
    part_1_answer = part_1(lines)
    assert part_1_answer == 5

    part_2_answer = part_2(lines)
    assert part_2_answer == 12

    with open("day05/input.txt", "r") as file:
        input_text = file.read()
        lines = get_data(input_text)

        part_1_answer = part_1(lines)
        print(f"{part_1_answer = }")

        part_2_answer = part_2(lines)
        print(f"{part_2_answer = }")
