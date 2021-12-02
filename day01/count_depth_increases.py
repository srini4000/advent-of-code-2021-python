""" https://adventofcode.com/2021/day/1 """
from functools import reduce
import aocd  # type: ignore


def count_depth_increases(input_data: list[str]) -> int:
    count = 0

    def depth_increase(a: str, b: str):
        nonlocal count
        if int(b) > int(a):
            count = count + 1
        return b

    reduce(depth_increase, input_data)
    return count


def count_depth_increases_sliding_window(input_data: list[str]) -> int:
    def get_3_seq_sum(input_data: list[str], index: int) -> int:
        return (
            int(input_data[index])
            + int(input_data[index + 1])
            + int(input_data[index + 2])
        )

    data_len = len(input_data)
    seq_sums = (get_3_seq_sum(input_data, index) for index in range(0, data_len - 2))

    count = 0

    def depth_increase(a: int, b: int):
        nonlocal count
        if b > a:
            count = count + 1
        return b

    reduce(depth_increase, seq_sums)

    return count


def main_1():
    input_data = """\
199
200
208
210
200
207
240
269
260
263""".splitlines()
    assert count_depth_increases(input_data) == 7
    assert count_depth_increases_sliding_window(input_data) == 5


def main_2():
    input_data = aocd.get_data(year=2021, day=1).splitlines()  # type: ignore

    part_1_answer = count_depth_increases(input_data)
    print(f"{part_1_answer = }")

    part_2_answer = count_depth_increases_sliding_window(input_data)
    print(f"{part_2_answer = }")


if __name__ == "__main__":
    main_1()
    main_2()
