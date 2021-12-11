"""
--- Day 8: Seven Segment Search ---
https://adventofcode.com/2021/day/8
See day08/segments.png for picture of how this logic is coded.
"""
from dataclasses import dataclass

SEGMENT = str  # one segment. Example: 'b'
SEGMENTS = frozenset[SEGMENT]  # Example: {'c', 'f'} represents digit 1
DIGIT = int
COUNT = int


@dataclass(frozen=True)
class Digit7Segments:
    segments2digit: dict[SEGMENTS, DIGIT]

    @classmethod
    def from_string(cls, s: str):
        # easy mapping based on uniq count of segments
        segment_counts: dict[COUNT, DIGIT] = {2: 1, 4: 4, 3: 7, 7: 8}

        segments2digit: dict[SEGMENTS, DIGIT] = {}
        digit2segments: dict[DIGIT, SEGMENTS] = {}

        # map easy digits first
        for digit_str in s.split():
            segments: SEGMENTS = frozenset(digit_str)
            segments_len = len(segments)
            if segments_len in segment_counts:
                digit = segment_counts[segments_len]
                segments2digit[segments] = digit
                digit2segments[digit] = segments

        for digit_str in s.split():
            segments: SEGMENTS = frozenset(digit_str)
            segments_len = len(segments)
            if segments_len not in segment_counts:
                match (segments_len,
                       segments.issuperset(digit2segments[7]),
                       len(segments.intersection(digit2segments[4])) == 3,
                       segments.issuperset(digit2segments[4])):
                    case 5, True, _, _:
                        segments2digit[segments] = 3
                        digit2segments[3] = segments
                    case 5, False, True, _:
                        segments2digit[segments] = 5
                        digit2segments[5] = segments
                    case 5, False, False, _:
                        segments2digit[segments] = 2
                        digit2segments[2] = segments
                    case 6, _, _, True:
                        segments2digit[segments] = 9
                        digit2segments[9] = segments
                    case 6, True, _, False:
                        segments2digit[segments] = 0
                        digit2segments[0] = segments
                    case 6, False, _, False:
                        segments2digit[segments] = 6
                        digit2segments[6] = segments

        return cls(segments2digit)

    def decode(self, segments_str: str) -> DIGIT:
        segments = frozenset(segments_str)
        return self.segments2digit[segments]


def part_1(input_text: str) -> int:
    count = 0
    for line in input_text.splitlines():
        input_str, output_str = line.split(" | ")
        digit7segments = Digit7Segments.from_string(input_str)

        for output_digit_str in output_str.split():
            count += 1 if digit7segments.decode(output_digit_str) in [1, 4, 7, 8] else 0
    return count


def part_2(input_text: str) -> int:
    count = 0
    for line in input_text.splitlines():
        input_str, output_str = line.split(" | ")
        digit7segments = Digit7Segments.from_string(input_str)

        output_digits_str = ""
        for output_digit_str in output_str.split():
            output_digits_str += str(digit7segments.decode(output_digit_str))

        output_digits = int(output_digits_str)
        count += output_digits
    return count


if __name__ == "__main__":
    input_text = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

    part_1_answer = part_1(input_text)
    assert part_1_answer == 26

    part_2_answer = part_2(input_text)
    assert part_2_answer == 61229

    with open("day08/input.txt", "r") as file:
        input_text = file.read()

        part_1_answer = part_1(input_text)
        print(f"{part_1_answer = }")

        part_2_answer = part_2(input_text)
        print(f"{part_2_answer = }")
