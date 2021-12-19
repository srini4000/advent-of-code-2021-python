"""
--- Day 10: Syntax Scoring ---
https://adventofcode.com/2021/day/10
"""
from collections import deque
from statistics import median


def part_1(input_text: str) -> int:
    score = 0
    scoring_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
    close_open_mapping = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    for line in input_text.splitlines():
        stack: deque[str] = deque()
        for char in line:
            if char not in close_open_mapping:
                # starts new open char
                stack.append(char)
            else:
                top_of_stack = stack[-1]
                if close_open_mapping[char] != top_of_stack:
                    # found first mismatch
                    score += scoring_map[char]
                    # print(f"Expected {top_of_stack}, but found {char} instead.")
                    break  # break inner loop. Go to process new line
                else:
                    stack.pop()

    return score


def part_2(input_text: str) -> int:
    scores: list[int] = []
    scoring_map = {"(": 1, "[": 2, "{": 3, "<": 4}
    close_open_mapping = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    for line in input_text.splitlines():
        stack: deque[str] = deque()
        score = 0
        for char in line:
            if char not in close_open_mapping:
                # starts new open char
                stack.append(char)
            else:
                top_of_stack = stack[-1]
                if close_open_mapping[char] != top_of_stack:
                    # found first mismatch
                    break  # break inner loop. Ignore corrupt lines in part2. Go to process new line
                else:
                    stack.pop()
        else:
            # this part executes only for incomplete lines
            # for each char left in stack, calculate the score
            while len(stack) != 0:
                top_of_stack = stack.pop()
                score = 5 * score + scoring_map[top_of_stack]
            scores.append(score)

    return int(median(scores))


if __name__ == "__main__":
    input_text = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

    part_1_answer = part_1(input_text)
    assert part_1_answer == 26397
    part_2_answer = part_2(input_text)
    assert part_2_answer == 288957

    with open("day10/input.txt") as file:
        input_text = file.read()

        part_1_answer = part_1(input_text)
        print(f"{part_1_answer = }")

        part_2_answer = part_2(input_text)
        print(f"{part_2_answer = }")
