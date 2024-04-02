# coding: utf-8
with open("input1") as f:
    lines = f.readlines()
measurements = [int(line.strip()) for line in lines]
increased, previous = 0, measurements[0]
for measurement in measurements:
    if measurement > previous:
        increased += 1
    previous = measurement
print("part 1:", increased)

increased, previous1, previous2, previous_sum = 0, 0, 0, 0
for index, measurement in enumerate(measurements):
    three_sum = previous2 + previous1 + measurement
    if index > 2 and three_sum > previous_sum:
        increased += 1
    previous2, previous1, previous_sum = previous1, measurement, three_sum
print("part 2:", increased)
