"""
--- Day 12: Passage Pathing ---
https://adventofcode.com/2021/day/12

"""
from dataclasses import dataclass
from collections import defaultdict, deque
from typing import TypeAlias

NODE: TypeAlias = str
GRAPH: TypeAlias = defaultdict[NODE, list[NODE]]

STACKNODE: TypeAlias = tuple[NODE, set[NODE]]
STACK: TypeAlias = deque[STACKNODE]

STACKNODE_2: TypeAlias = tuple[NODE, set[NODE], bool]
STACK_2: TypeAlias = deque[STACKNODE_2]


@dataclass
class Graph:
    g: GRAPH

    @classmethod
    def from_string(cls, s: str):
        g: GRAPH = defaultdict(list)
        for line in s.splitlines():
            node_1, node_2 = line.split("-")
            if node_2 != "start":
                g[node_1].append(node_2)
            if node_1 != "start":
                g[node_2].append(node_1)
        return cls(g)

    def part_1_count_paths_from(self, start: NODE) -> int:
        path_count = 0

        # using stack with dfs algo
        stack: STACK = deque()
        # store the current node 'start'
        # second part of tuple '{start}' represents set of nodes that are part of path
        stack.append((start, {start}))

        while stack:
            node, visited = stack.pop()
            if node == "end":
                path_count += 1
                continue
            for neighbor in self.g[node]:
                if neighbor in visited and neighbor.islower():
                    # lower case neighbor is already visited
                    continue
                # add neighbor to stack and mark this neighbor to visited
                # set in this particular path
                new_visited = visited | {neighbor}
                stack.append((neighbor, new_visited))

        return path_count

    def part_2_count_paths_from(self, start: NODE) -> int:
        path_count = 0

        # using stack with dfs algo
        stack: STACK_2 = deque()
        # store the current node 'start'
        # second part of tuple '{start}' represents set of nodes that are part of path
        # third part of tuple 'False' represents if there is a lower case node already twice
        stack.append((start, {start}, False))

        while stack:
            node, visited, double = stack.pop()
            if node == "end":
                path_count += 1
                continue
            for neighbor in self.g[node]:
                if neighbor not in visited or neighbor.isupper():
                    new_visited = visited | {neighbor}
                    stack.append((neighbor, new_visited, double))
                    continue

                if double:
                    continue
                new_visited = visited | {neighbor}
                stack.append((neighbor, new_visited, True))

        return path_count


if __name__ == "__main__":
    input_text = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    graph = Graph.from_string(input_text)
    part_1_answer = graph.part_1_count_paths_from("start")
    assert part_1_answer == 10
    part_2_answer = graph.part_2_count_paths_from("start")
    assert part_2_answer == 36

    with open("day12/input.txt") as file:
        input_text = file.read()
        graph = Graph.from_string(input_text)
        part_1_answer = graph.part_1_count_paths_from("start")
        print(f"{part_1_answer = }")
        part_2_answer = graph.part_2_count_paths_from("start")
        print(f"{part_2_answer = }")
