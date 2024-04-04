# coding: utf-8
def binary_to_decimal(bits: list) -> int:
    return sum([bit * 2**index for index, bit in enumerate(bits[::-1])])


def get_most_common_bit(position: int, numbers: list) -> int:
    bits_on_position = [number[position] for number in numbers]
    one_bit_frequency = sum(bits_on_position) / len(bits_on_position)
    if one_bit_frequency == 0.5:  # if equal, return 1
        return 1
    else:
        return round(one_bit_frequency)


with open("input3") as f:
    numbers = [line.strip() for line in f.readlines()]

numbers = [[int(bit) for bit in list(number)] for number in numbers]
number_of_bits, length = len(numbers[0]), len(numbers)
bits = [0] * number_of_bits

for index in range(number_of_bits):
    bits[index] = sum([number[index] for number in numbers])

gamma = [round(bit / length) for bit in bits]
epsilon = [int(not bit) for bit in gamma]
gamma_decimal = binary_to_decimal(gamma)
epsilon_decimal = binary_to_decimal(epsilon)

print(
    f"part 1: gamma: {gamma_decimal}, epsilon: {epsilon_decimal}, solution: {gamma_decimal * epsilon_decimal}"
)

oxygen = numbers.copy()
for index in range(number_of_bits):
    most_common_bit = get_most_common_bit(index, oxygen)
    oxygen = list(filter(lambda bits: bits[index] == most_common_bit, oxygen))
    if len(oxygen) == 1:
        break
oxygen = oxygen[0]
oxygen_decimal = binary_to_decimal(oxygen)

co2 = numbers.copy()
for index in range(number_of_bits):
    most_common_bit = get_most_common_bit(index, co2)
    co2 = list(filter(lambda bits: bits[index] != most_common_bit, co2))
    if len(co2) == 1:
        break
co2 = co2[0]
co2_decimal = binary_to_decimal(co2)

print(
    f"part 2: oxygen: {oxygen_decimal}, CO2: {co2_decimal}, solution: {oxygen_decimal * co2_decimal}"
)
