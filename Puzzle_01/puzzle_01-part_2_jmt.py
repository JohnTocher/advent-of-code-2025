"""Advent of code 2025 - Puzzle 01

https://adventofcode.com/2025/day/1

John Tocher
Solution to puzzle 01 part 2
"""

# INPUT_FILE_NAME = "puzzle_01_input_01_sample.txt"
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
    total_zero_crossings = 0
    for each_move in puzzle_input:
        count_moves += 1
        count_at_zero = 0
        count_zero_cross = 0
        move_dir = each_move[0:1]
        move_size = int(each_move[1:]) % 100
        count_zero_cross = int(int(each_move[1:]) / 100)
        if move_dir == "R":
            new_pos = dial_pos + move_size
            if new_pos > 100:
                count_zero_cross += 1
                # print(f"Crossing zero R: {count_zero_cross}")
        elif move_dir == "L":
            new_pos = dial_pos - move_size
            if new_pos < 0 and dial_pos > 0:
                count_zero_cross += 1
                # print(f"Crossing zero L: {count_zero_cross}")
        else:
            assert False, f"Unexpected input at line: {count_moves}"

        dial_pos = new_pos % 100

        if dial_pos == 0:
            count_at_zero += 1
        total_zero_crossings += count_at_zero + count_zero_cross

        print(
            f"The dial is rotated {each_move} to point at {dial_pos}. Total: {total_zero_crossings} zero crossings"
        )

    print(f"Result is: {total_zero_crossings} zero crossings or stops")


if __name__ == "__main__":
    solve_puzzle()
