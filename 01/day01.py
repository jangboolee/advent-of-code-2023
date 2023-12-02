import os
from operator import itemgetter


with open(os.path.join(".", "01", "input.txt"), "r", encoding="utf-8") as f:
    lines = [line.rstrip() for line in f.readlines()]

# Part one

cal_values_0 = []
for line in lines:
    str_cal_value = ""
    for char in line:
        if char.isnumeric():
            str_cal_value += char
            break
    for char in line[::-1]:
        if char.isnumeric():
            str_cal_value += char
            break
    cal_values_0.append(int(str_cal_value))

print(f"Pt. 1 - sum of calibration values: {sum(cal_values_0)}")


# Part two


def find_first_cal_value(line: str, reverse: bool) -> str:
    """Helper function to find the first or last calibration value in a line of
    the calibration document

    Args:
        line (str): One line in the calibration document
        reverse (bool): True to find the last calibration value, False to find
            the first calibration value

    Returns:
        str: The character for the first of last calibration value
    """

    # Digits spelled out with letters
    str_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    # Find existing literal digits in the line and their indices
    found_str_digits = []
    for str_digit in str_digits:
        if str_digit in line:
            found_str_digits.extend(
                [
                    (i, str_digit)
                    for i in range(len(line))
                    if line.startswith(str_digit, i)
                ]
            )
    # Find integer characters in the line and their indices
    found_int_chars = [
        (i, char) for i, char in enumerate(line) if char.isnumeric()
    ]

    # Get largest index items to find the last calibration value
    if reverse:
        # If both string digits and integer characters are found
        if found_str_digits and found_int_chars:
            # Get the item with the maximum index from both types
            rel_str_digit = max(found_str_digits, key=itemgetter(0))
            rel_int_char = max(found_int_chars, key=itemgetter(0))
            # Get whichever item has the larger index
            if rel_str_digit[0] > rel_int_char[0]:
                return str_digits[rel_str_digit[1]]
            else:
                return rel_int_char[1]
        # If only string digits are found
        elif found_str_digits:
            # Get the string digit with the maximum index
            rel_str_digit = max(found_str_digits, key=itemgetter(0))
            return str_digits[rel_str_digit[1]]
        # If only integer characters are found
        else:
            # Get the integer character with the maximum index
            return max(found_int_chars, key=itemgetter(0))[1]
    # Get smallest index items to find the first calibration value
    else:
        # If both string digits and integer characters are found
        if found_str_digits and found_int_chars:
            # Get the item with the minimum index from both types
            rel_str_digit = min(found_str_digits, key=itemgetter(0))
            rel_int_char = min(found_int_chars, key=itemgetter(0))
            # Get whichever item has the smaller index
            if rel_str_digit[0] < rel_int_char[0]:
                return str_digits[rel_str_digit[1]]
            # If only string digits are found
            else:
                # Get the string digit with the minimum index
                return rel_int_char[1]
        # If only integer characters are found
        elif found_str_digits:
            rel_str_digit = min(found_str_digits, key=itemgetter(0))
            return str_digits[rel_str_digit[1]]
        # Get the integer character with the maximum index
        else:
            return min(found_int_chars, key=itemgetter(0))[1]


cal_values_1 = []
for line in lines:
    str_cal_value = ""
    str_cal_value += find_first_cal_value(line, False)
    str_cal_value += find_first_cal_value(line, True)
    cal_values_1.append(int(str_cal_value))

print(f"Pt. 2 - sum of calibration values: {sum(cal_values_1)}")
