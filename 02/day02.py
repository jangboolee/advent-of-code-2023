import os
import re
from math import prod


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


def parse_input(data: list) -> dict:
    """Function to parse the entire input file

    Args:
        data (list): List of lists representing the input file's contents

    Returns:
        dict: Dictionary with each key-value pair reprsenting a single game
    """

    def parse_line(line: str) -> tuple:
        """Helper to parses one line of the game result

        Args:
            line (str): One line of the game result

        Returns:
            tuple: Parsed game ID as the first item, and a list of dictionaries
                with each dictionary being one set for the game
        """

        # Separate game ID and result, then parse game ID
        game_id, result = line.split(": ")
        game_id = int(game_id.replace("Game ", ""))

        # Parse game results as a dictionary per set using regex
        sets_raw = [set_.split(", ") for set_ in result.split("; ")]
        pattern = re.compile(r"(\d+)\s(\w+)")
        game_result = []
        for set_ in sets_raw:
            set_result = {"red": 0, "green": 0, "blue": 0}
            for dice_count in set_:
                matched = re.match(pattern, dice_count)
                count = int(matched.group(1))
                color = matched.group(2)
                set_result[color] += count
            game_result.append(set_result)

        return (game_id, game_result)

    # Parse entire input data
    games = {}
    for line in data:
        game_id, game_result = parse_line(line)
        games[game_id] = game_result

    return games


def get_max_cubes_per_game(game: list) -> dict:
    """Function to get the maximum number of cubes per color for each game

    Args:
        game (list): A list of dictionaries, representing the sets played
            in one game

    Returns:
        dict: A dictionary of the maximum marbles observed for each game
            per color
    """

    game_max = {"red": 0, "green": 0, "blue": 0}
    for _set in game:
        for color, count in _set.items():
            game_max[color] = max(count, game_max[color])

    return game_max


def solve_part_one(games: dict, red: int, green: int, blue: int) -> int:
    """Function to group calculations for part 1

    Args:
        games (dict): Dictionary of all parsed game records
        red (int): Count cut-off for red marbles
        green (int): Count cut-off for green marbles
        blue (int): Count cut-off for blue marbles

    Returns:
        int: Sum of game IDs that are possible
    """

    def check_game_possibility(
        game_max: dict, red: int, green: int, blue: int
    ) -> bool:
        """Helper to check which games are theoretically possible

        Args:
            game_max (dict): Dictionary of the maximum marbles observed for
                each game per color
            red (int): Count cut-off for red marbles
            green (int): Count cut-off for green marbles
            blue (int): Count cut-off for blue marbles

        Returns:
            bool: True if the game is possible (there are no subsets of marbles
                observed with count of marbles greater than the color cut-off
                values), False if not
        """

        return (
            game_max["red"] <= red
            and game_max["green"] <= green
            and game_max["blue"] <= blue
        )

    possible_ids = []
    for game_id, game_result in games.items():
        game_cube_max = get_max_cubes_per_game(game_result)
        if check_game_possibility(game_cube_max, red, green, blue):
            possible_ids.append(game_id)
    return sum(possible_ids)


def solve_part_two(games: dict) -> int:
    cube_powers = []
    for game_result in games.values():
        game_max = get_max_cubes_per_game(game_result)
        cube_powers.append(prod(game_max.values()))
    return sum(cube_powers)


def main() -> None:
    # Read input file
    lines = read_input("02")

    # Parse input file
    games = parse_input(lines)

    # Solve part one
    part_one_ans = solve_part_one(games=games, red=12, green=13, blue=14)
    print(part_one_ans)

    # Solve part two
    part_two_ans = solve_part_two(games)
    print(part_two_ans)


if __name__ == "__main__":
    main()
