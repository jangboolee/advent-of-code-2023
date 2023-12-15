import os
import re


def read_input(folder_name: str) -> list:
    """Function to read in the input file as a list of lists

    Args:
        folder_name (str): Folder name where the day's puzzle files are stored

    Returns:
        list: List of lists with each list containing one line of the input
            file's contents
    """

    with open(
        os.path.join(".", folder_name, "input.txt"), "r", encoding="utf-8"
    ) as f:
        return [line.rstrip() for line in f.readlines()]


def solve_part_one() -> int:
    pass


def solve_part_two() -> int:
    pass


def find_symbol_coords(data: list) -> list:
    symbol_coords = []
    for row_num, line in enumerate(data):
        for col_num, char in enumerate(line):
            if not char.isnumeric() and char != ".":
                symbol_coords.append((row_num, col_num))

    return symbol_coords


def find_part_numbers(data: list, symbol_coords: list) -> list:
    def get_adjacent_coords(coords: tuple) -> list:
        row_num = coords[0]
        col_num = coords[1]

        adjacent_coords = [
            (row_num - 1, col_num - 1),
            (row_num - 1, col_num),
            (row_num - 1, col_num + 1),
            (row_num, col_num - 1),
            (row_num, col_num + 1),
            (row_num + 1, col_num - 1),
            (row_num + 1, col_num),
            (row_num + 1, col_num + 1),
        ]

        return adjacent_coords

    part_numbers = []
    for symbol_coord in symbol_coords:
        part_number_coords = get_adjacent_coords(symbol_coord)
        for row_num, col_num in part_number_coords:
            if data[row_num][col_num].isnumeric():
                part_numbers.append(int(data[row_num][col_num]))

    for line in data:
        nums = re.findall(r"\d+", line)
        for num in nums:
            num_index_range = range(
                line.index(num), line.index(num) + len(num) + 1
            )

    return part_numbers


def main() -> None:
    lines = read_input("03")
    print("")

    symbol_coords = find_symbol_coords(lines)
    part_numbers = find_part_numbers(lines, symbol_coords)
    print("")


if __name__ == "__main__":
    main()
