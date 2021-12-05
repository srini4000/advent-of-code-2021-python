"""
https://adventofcode.com/2021/day/4
"""
# Type Aliases
CALLED_STATUS = bool
BOARD_CELL = tuple[int, CALLED_STATUS]
BOARD_LINE = list[BOARD_CELL]
BOARD = list[BOARD_LINE]
BOARDS = list[BOARD]
CALLS = list[int]


def load_input_text(input_text: str) -> tuple[CALLS, BOARDS]:
    (calls_str, *boards_str) = input_text.split("\n\n")
    calls: CALLS = [int(call_str) for call_str in calls_str.split(",")]

    boards: BOARDS = []
    for board_str in boards_str:
        board: BOARD = []
        for line in board_str.splitlines():
            cells = [(int(num_str), False) for num_str in line.split()]
            board.append(cells)
        boards.append(board)
    return (calls, boards)


def mark_board(call: int, board: BOARD) -> bool:
    """Returns True if bingo"""
    for row, board_line in enumerate(board):
        for column, cell in enumerate(board_line):
            num, called_status = cell
            if num == call and not called_status:
                called_status = True
                board_line[column] = (call, called_status)
                return check_board(board, row, column)

    return False


def check_board(board: BOARD, row: int, column: int) -> bool:
    n = len(board)  # board is n x n grid
    if all(board[row][j][1] for j in range(n)) or all(
        board[i][column][1] for i in range(n)
    ):
        return True
    return False


def calculate_score(call: int, board: BOARD) -> int:
    n = len(board)  # board is n x n grid
    return sum(board[i][j][0] for i in range(n) for j in range(n) if not board[i][j][1])


def part_1(calls: CALLS, boards: BOARDS) -> int:
    for call in calls:
        for board in boards:
            if mark_board(call, board):
                return call * calculate_score(call, board)
    return -1


def part_2(calls: CALLS, boards: BOARDS) -> int:
    boards_count = len(boards)
    winning_boards: set[int] = set()
    for call in calls:
        for board_id, board in enumerate(boards):
            if mark_board(call, board):
                winning_boards.add(board_id)
                if boards_count == len(winning_boards):
                    return call * calculate_score(call, board)
    return -1


if __name__ == "__main__":
    input_text = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
    (calls, boards) = load_input_text(input_text)

    part_1_answer = part_1(calls, boards)
    assert part_1_answer == 4512

    (calls, boards) = load_input_text(input_text)
    part_2_answer = part_2(calls, boards)
    assert part_2_answer == 1924

    with open("day04/input.txt", "r") as file:
        input_text = file.read()

        (calls, boards) = load_input_text(input_text)
        part_1_answer = part_1(calls, boards)
        print(f"{part_1_answer = }")

        (calls, boards) = load_input_text(input_text)
        part_2_answer = part_2(calls, boards)
        print(f"{part_2_answer = }")
