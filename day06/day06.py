"""
--- Day 6: Lanternfish ---
https://adventofcode.com/2021/day/6
"""
from dataclasses import dataclass


@dataclass
class State:
    timers: list[int]
    days: int = 0

    def add_day(self, days: int = 1):
        for _ in range(days):
            new_timers: list[int] = []
            for index, timer in enumerate(self.timers):
                if timer == 0:
                    self.timers[index] = 6
                    new_timers.append(8)
                else:
                    self.timers[index] -= 1
            self.timers += new_timers
            self.days += 1

    def __len__(self):
        return len(timers)


if __name__ == "__main__":
    input_text = "3,4,3,1,2"
    timers = [int(timer) for timer in input_text.split(",")]
    state = State(timers)
    state.add_day(80)
    assert len(state) == 5934

    with open("day06/input.txt") as file:
        input_text = file.read()
        timers = [int(timer) for timer in input_text.split(",")]
        state = State(timers)
        state.add_day(80)
        part_1_answer = len(state)
        print(f"{part_1_answer = }")
