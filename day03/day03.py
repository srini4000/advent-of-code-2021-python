"""
https://adventofcode.com/2021/day/3
"""

from collections import Counter


def part_1(input_text: str) -> int:
    input_data = input_text.splitlines()
    counters: list[Counter[str]] = [Counter() for _ in range(len(input_data[0]))]
    for binary_str in input_data:
        for position, digit in enumerate(binary_str):
            position_counter = counters[position]
            position_counter[digit] += 1

    gamma_rate_str = ""
    epsilon_rate_str = ""
    for position_counter in counters:
        # print(f"{position_counter.most_common()[0][0] = }")
        gamma_rate_str += position_counter.most_common()[0][0]

        # print(f"{position_counter.most_common()[-1][0] = }")
        epsilon_rate_str += position_counter.most_common()[-1][0]

    # print(f"{gamma_rate_str = }")
    # print(f"{int(gamma_rate_str,2) = }")

    # print(f"{epsilon_rate_str = }")
    # print(f"{int(epsilon_rate_str,2) = }")

    power_consumption = int(gamma_rate_str, 2) * int(epsilon_rate_str, 2)
    return power_consumption


if __name__ == "__main__":
    input_text = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
    assert part_1(input_text) == 198

    with open("day03/input.txt", "r") as file:
        input_text = file.read()
        part_1_answer = part_1(input_text)
        print(f"{part_1_answer = }")
