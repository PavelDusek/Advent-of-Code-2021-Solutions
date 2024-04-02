# coding: utf-8
with open("input2") as f:
    lines = f.readlines()
commands = [line.strip().split(" ") for line in lines]
commands = [(command, int(value)) for (command, value) in commands]

# Part 1
horizontal, depth = 0, 0
for (command, value) in commands:
    match command:
        case "forward":
            horizontal_coeff, depth_coeff = 1, 0
        case "down":
            horizontal_coeff, depth_coeff = 0, 1
        case "up":
            horizontal_coeff, depth_coeff = 0, -1
    horizontal += horizontal_coeff * value
    depth += depth_coeff * value
solution = horizontal * depth
print(f"part 1 | horizontal: {horizontal}, depth: {depth}, solution: {solution}")

# Part 2
horizontal, depth, aim = 0, 0, 0
for (command, value) in commands:
    match command:
        case "forward":
            horizontal += value
            depth += aim * value
        case "down":
            aim += value
        case "up":
            aim -= value
solution = horizontal * depth
print(f"part 2 | horizontal: {horizontal}, depth: {depth}, solution: {solution}")
