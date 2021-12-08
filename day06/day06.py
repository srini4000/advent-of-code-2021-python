"""
--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6
"""
from dataclasses import dataclass
from collections import Counter


@dataclass
class State:
    counter: Counter[int]
    days: int = 0

    def add_days(self, days: int = 1):
        for _ in range(days):
            new_counter: Counter[int] = Counter()
            for timer, count in self.counter.items():
                if timer == 0:
                    self.counter[0] -= count  # these 0 go away
                    new_counter[6] += count  # 0 becomes 6
                    new_counter[8] += count  # Also, new childs are added with life of 8
                else:
                    self.counter[timer] -= count
                    new_counter[timer - 1] += count
            self.counter += new_counter
            self.days += 1

    def __len__(self):
        return sum(self.counter.values())


if __name__ == "__main__":
    input_text = "3,4,3,1,2"
    timers = [int(timer) for timer in input_text.split(",")]
    counter = Counter(timers)
    state = State(counter)
    state.add_days(80)

    part_1_answer = len(state)
    assert len(state) == 5934

    state.add_days(256 - 80)
    part_2_answer = len(state)
    assert part_2_answer == 26984457539

    with open("day06/input.txt") as file:
        input_text = file.read()
        timers = [int(timer) for timer in input_text.split(",")]
        counter = Counter(timers)
        state = State(counter)

        state.add_days(80)
        part_1_answer = len(state)
        print(f"{part_1_answer = }")

        state.add_days(256 - 80)
        part_2_answer = len(state)
        print(f"{part_2_answer = }")
