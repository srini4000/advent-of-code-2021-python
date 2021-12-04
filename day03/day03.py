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


"""
find_rating is a recursive function
- apply bit criteria to each bit_position
- If multiple nums are found, then search filtered nums for next bit position
using recursion
"""


def find_rating(input_data: list[str], bit_position: int, is_oxygen: bool) -> int:
    n = len(input_data)
    n_bits = len(input_data[0])
    for c in range(bit_position, n_bits):
        # c is current_column being processed
        column_nums = [input_data[i] for i in range(n)]
        column_bits = [s[bit_position] for s in column_nums]
        if is_oxygen:
            # If 0 and 1 are equally common
            [(bit, count1), (_, count2)] = Counter(column_bits).most_common(2)
            if count1 == count2:
                keep_bit = "1"
            else:
                keep_bit = bit
        else:
            # If 0 and 1 are equally common
            [(_, count1), (bit, count2)] = Counter(column_bits).most_common()[-2:]
            if count1 == count2:
                keep_bit = "0"
            else:
                keep_bit = bit
        input_data_new = [num for num in column_nums if num[c] == keep_bit]
        if len(input_data_new) == 1:
            return int(input_data_new[0], 2)
        return find_rating(input_data_new, bit_position + 1, is_oxygen)
    return -1


def part_2(input_text: str) -> int:
    input_data = input_text.splitlines()

    oxygen_rating = find_rating(input_data, 0, is_oxygen=True)
    co2_rating = find_rating(input_data, 0, is_oxygen=False)
    life_rating = oxygen_rating * co2_rating
    return life_rating


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
    assert part_2(input_text) == 230

    with open("day03/input.txt", "r") as file:
        input_text = file.read()

        part_1_answer = part_1(input_text)
        print(f"{part_1_answer = }")

        part_2_answer = part_2(input_text)
        print(f"{part_2_answer = }")
