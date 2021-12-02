""" https://adventofcode.com/2021/day/1 """


def get_input_data(input_text: str) -> list[int]:
    depths = [int(line) for line in input_text.splitlines()]
    return depths


def count_depth_increases(depths: list[int]) -> int:
    count = 0

    for (a, b) in zip(depths, depths[1:]):
        if b > a:
            count += 1
    return count


def count_depth_increases_sliding_window(depths: list[int]) -> int:
    count = 0
    window_sums = [a + b + c for (a, b, c) in zip(depths, depths[1:], depths[2:])]
    for (a, b) in zip(window_sums, window_sums[1:]):
        if b > a:
            count += 1

    return count


if __name__ == "__main__":
    input_text = """\
199
200
208
210
200
207
240
269
260
263"""
    depths = get_input_data(input_text)
    assert count_depth_increases(depths) == 7
    assert count_depth_increases_sliding_window(depths) == 5

    with open("day01/input.txt", "r") as file:
        input_text = file.read()
        depths = get_input_data(input_text)

        part_1_answer = count_depth_increases(depths)
        print(f"{part_1_answer = }")

        part_2_answer = count_depth_increases_sliding_window(depths)
        print(f"{part_2_answer = }")
