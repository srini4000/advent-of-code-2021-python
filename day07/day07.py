"""
--- Day 7: The Treachery of Whales ---
https://adventofcode.com/2021/day/7
"""
import statistics


def part_1(positions: list[int], median: int) -> int:
    return sum(abs(position - median) for position in positions)


def calculate_fuel(target: int, position: int) -> int:
    d = abs(target - position)
    return d * (d + 1) // 2


def part_2(positions: list[int], mean: int) -> int:
    potential_targets = (int(mean - 0.5), int(mean + 0.5))
    return min(
        sum(calculate_fuel(target, position) for position in positions)
        for target in potential_targets
    )


if __name__ == "__main__":
    input_text = "16,1,2,0,4,2,7,1,2,14"
    positions = [int(position_str) for position_str in input_text.split(",")]

    median = round(statistics.median(positions))
    part_1_answer = part_1(positions, median)
    assert part_1_answer == 37

    mean = round(statistics.mean(positions))
    part_2_answer = part_2(positions, mean)
    assert part_2_answer == 168

    with open("day07/input.txt", "r") as file:
        input_text = file.read()
        positions = [int(position_str) for position_str in input_text.split(",")]

        median = round(statistics.median(positions))
        part_1_answer = part_1(positions, median)
        print(f"{part_1_answer = }")

        mean = round(statistics.mean(positions))
        part_2_answer = part_2(positions, mean)
        print(f"{part_2_answer = }")
