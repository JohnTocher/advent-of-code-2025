"""Advent of code 2025 - Puzzle 01

https://adventofcode.com/2025/day/1

John Tocher
Solution to puzzle 01 part 1
"""

INPUT_FILE_NAME = "puzzle_01_input_01.txt"


def read_input_data():
    # Read the puzzle input from a text file
    count_lines = 0
    list_of_rotations = list()

    for single_line in open(INPUT_FILE_NAME, "r").readlines():
        count_lines += 1
        clean_line = single_line.strip()
        list_of_rotations.append(clean_line)

    return list_of_rotations


def solve_puzzle():
    # Main solving logic
    puzzle_input = read_input_data()
    # print(puzzle_input)
    assert len(puzzle_input[0]) == len(puzzle_input[1]), "Bad input!"

    dial_pos = 50
    count_moves = 0
    count_at_zero = 0
    for each_move in puzzle_input:
        count_moves += 1
        move_dir = each_move[0:1]
        move_size = int(each_move[1:]) % 100
        # print(f"Move {count_moves:04} is {each_move}")
        if move_dir == "R":
            move_distance = move_size
        elif move_dir == "L":
            move_distance = 100 - move_size
        else:
            assert False, f"Unexpected input at line: {count_moves}"
        new_pos = (dial_pos + move_distance) % 100
        if new_pos == 0:
            count_at_zero += 1
        print(
            f"The dial is rotated {each_move} ({move_distance}) to point at {new_pos}."
        )
        dial_pos = new_pos

    print(f"Result is: {count_at_zero} at zero")


if __name__ == "__main__":
    solve_puzzle()
