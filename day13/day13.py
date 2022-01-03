"""
--- Day 13: Transparent Origami ---
https://adventofcode.com/2021/day/13
"""

from dataclasses import dataclass
from typing import TypeAlias
from operator import itemgetter

DOT: TypeAlias = tuple[int, int]
SHEET: TypeAlias = set[DOT]
IS_X_AXIS = bool
FOLDS: TypeAlias = list[tuple[int, IS_X_AXIS]]


@dataclass
class Sheet:
    sheet: SHEET
    folds: FOLDS

    @classmethod
    def from_string(cls, input_text: str):
        dots, folds_input = input_text.split("\n\n")
        sheet: SHEET = set()
        for dot in dots.splitlines():
            x_str, y_str = dot.split(",")
            x, y = int(x_str), int(y_str)
            sheet.add((x, y))

        folds: FOLDS = []
        for fold_line in folds_input.splitlines():
            fold_str = fold_line.removeprefix("fold along ")
            axis, fold_count_str = fold_str.split("=")
            fold_count = int(fold_count_str)
            folds.append((fold_count, axis == "x"))

        return cls(sheet, folds)

    def fold(self, distance: int, is_xaxis: bool):
        new_sheet: SHEET = set()
        for x, y in self.sheet:
            if is_xaxis:
                if x > distance:
                    x = distance - (x - distance)
            else:
                if y > distance:
                    y = distance - (y - distance)
            new_sheet.add((x, y))
        self.sheet = new_sheet

    def __len__(self) -> int:
        return len(self.sheet)

    def print(self):
        maxx = max(map(itemgetter(0), self.sheet))
        maxy = max(map(itemgetter(1), self.sheet))

        out = ""
        for y in range(maxy + 1):
            for x in range(maxx + 1):
                out += "#" if (x, y) in self.sheet else " "
            out += "\n"

        print(out, end="")

    def part_1(self) -> int:
        distance, is_x_axis = self.folds[0]
        self.fold(distance, is_x_axis)
        return len(self)

    def part_2(self):
        for distance, is_x_axis in self.folds:
            self.fold(distance, is_x_axis)
        self.print()


if __name__ == "__main__":
    input_text = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""
    sheet = Sheet.from_string(input_text)
    part_1_answer = sheet.part_1()
    assert part_1_answer == 17

    sheet = Sheet.from_string(input_text)
    sheet.part_2()

    with open("day13/input.txt") as file:
        input_text = file.read()
        sheet = Sheet.from_string(input_text)
        part_1_answer = sheet.part_1()
        print(f"{part_1_answer = }")

        sheet.part_2()
