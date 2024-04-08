# coding: utf-8
with open("input7") as f:
    crabs = [int(crab) for crab in f.read().split(",")]

lowest_fuel, best_position = (
    sum([abs(crab - (max(crabs) + 1)) for crab in crabs]),
    max(crabs) + 1,
)
for position in range(max(crabs)):
    fuel = sum([abs(crab - position) for crab in crabs])
    if fuel < lowest_fuel:
        lowest_fuel, best_position = fuel, position
print(f"part 1 | fuel: {lowest_fuel}, position: {best_position}")


def progressive_cost(position1: int, position2: int) -> int:
    return sum([step for step in range(abs(position2 - position1) + 1)])


lowest_fuel, best_position = (
    sum([progressive_cost(crab, max(crabs) + 1) for crab in crabs]),
    max(crabs) + 1,
)
for position in range(max(crabs)):
    fuel = sum([progressive_cost(crab, position) for crab in crabs])
    if fuel < lowest_fuel:
        lowest_fuel, best_position = fuel, position
print(f"part 2 | fuel: {lowest_fuel}, position: {best_position}")
