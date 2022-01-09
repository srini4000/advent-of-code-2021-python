from dataclasses import dataclass
from collections import Counter
from typing import ClassVar, TypeAlias

ELEMENT: TypeAlias = str  # represents on character string
PAIR: TypeAlias = tuple[ELEMENT, ELEMENT]
RULES: TypeAlias = dict[PAIR, ELEMENT]
POLYMER: TypeAlias = Counter[PAIR]


@dataclass
class Polymer:
    template: str
    data: POLYMER
    rules: RULES
    step_count: ClassVar = 0

    @classmethod
    def from_string(cls, input_text: str):
        data: POLYMER = Counter()
        data_str, rules_str = input_text.split("\n\n")
        for e1, e2 in zip(data_str, data_str[1:]):
            data[(e1, e2)] += 1

        rules: RULES = dict()
        for rule_str in rules_str.splitlines():
            e1e2, e3 = rule_str.split(" -> ")
            e1, e2 = e1e2
            rules[(e1, e2)] = e3
        return cls(data_str, data, rules)

    def step(self):
        new_data: POLYMER = Counter()
        for e1, e2 in self.data:
            if self.data[(e1, e2)] != 0:
                count = self.data[(e1, e2)]
                e3 = self.rules[(e1, e2)]  # new middle element
                new_data[(e1, e3)] += count
                new_data[(e3, e2)] += count
        self.data = new_data
        Polymer.step_count += 1

    def apply_steps(self, step_count: int):
        for _ in range(step_count):
            self.step()

    def get_answer(self) -> int:
        element_counter: Counter[ELEMENT] = Counter()
        for e1, e2 in self.data:
            element_counter[e1] += self.data[(e1, e2)]
        last_element = self.template[-1]
        element_counter[last_element] += 1

        most_commons = element_counter.most_common()
        most_common_quantity = most_commons[0][1]
        least_common_quantity = most_commons[-1][1]
        return most_common_quantity - least_common_quantity

    def part_1(self) -> int:
        self.apply_steps(10)
        return self.get_answer()

    def part_2(self) -> int:
        self.apply_steps(40)
        return self.get_answer()


if __name__ == "__main__":
    # with open("day14/sample.txt") as file:
    with open("day14/input.txt") as file:
        input_text = file.read()
        polymer = Polymer.from_string(input_text)
        part_1_answer = polymer.part_1()
        print(f"{part_1_answer = }")

        polymer = Polymer.from_string(input_text)
        part_2_answer = polymer.part_2()
        print(f"{part_2_answer = }")
