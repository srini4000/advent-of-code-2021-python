"""
https://adventofcode.com/2021/day/2
"""


def get_input_data(input_text: str) -> list[tuple[str, int]]:
    input_data: list[tuple[str, int]] = []
    for line in input_text.splitlines():
        (cmd, value_str) = line.split()
        input_data.append((cmd, int(value_str)))
    return input_data


def part_1(input_data: list[tuple[str, int]]) -> int:
    depth = 0
    forward_position = 0
    for (cmd, units) in input_data:
        match cmd:
            case 'forward':
               forward_position += units
            case 'up':
                depth  -= units
            case 'down':
                depth += units
    return depth*forward_position

def part_2(input_data: list[tuple[str, int]]) -> int:
    depth = 0
    forward_position = 0
    aim = 0

    for (cmd, units) in input_data:
        match cmd:
            case 'forward':
               forward_position += units
               depth += aim * units
            case 'up':
                aim -= units
            case 'down':
                aim += units
    return depth*forward_position

if __name__ == "__main__":
    input_text = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
    input_data = get_input_data(input_text)
    part_1_answer = part_1(input_data)
    assert part_1_answer == 150

    part_2_answer = part_2(input_data)
    assert part_2_answer == 900

    with open("day02/input.txt", "r") as file:
        input_text = file.read()
        input_data = get_input_data(input_text)

        part_1_answer = part_1(input_data)
        print(f"{part_1_answer = }")

        part_2_answer = part_2(input_data)
        print(f"{part_2_answer = }")