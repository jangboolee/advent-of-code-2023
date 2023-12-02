import os


with open(os.path.join(".", "01", "input.txt"), "r", encoding="utf-8") as f:
    lines = [line.rstrip() for line in f.readlines()]

# Part one

cal_values = []
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
    cal_values.append(int(str_cal_value))

print(f"sum of calibration values: {sum(cal_values)}")

# Part two
