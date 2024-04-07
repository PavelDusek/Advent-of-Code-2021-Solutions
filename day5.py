# coding: utf-8
from collections import defaultdict


class Line:
    def __init__(self, description):
        point1, point2 = description.split(" -> ")
        x1, y1 = point1.split(",")
        x2, y2 = point2.split(",")
        self.x1, self.y1, self.x2, self.y2 = int(x1), int(y1), int(x2), int(y2)

    def is_horizontal(self) -> bool:
        return self.y1 == self.y2

    def is_vertical(self) -> bool:
        return self.x1 == self.x2

    def is_diagonal(self) -> bool:
        return abs(self.x2 - self.x1) == abs(self.y2 - self.y1)

    def get_points(self) -> list:
        if self.is_horizontal():
            # add +1 to include the second point
            return [
                (x, self.y1)
                for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1)
            ]
        if self.is_vertical():
            # add +1 to include the second point
            return [
                (self.x1, y)
                for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1)
            ]
        if self.is_diagonal():
            if (self.x2 - self.x1) * (self.y2 - self.y1) > 0:
                # upper left, lower right
                return [
                    (min(self.x1, self.x2) + d, min(self.y1, self.y2) + d)
                    for d in range(0, max(self.x1, self.x2) - min(self.x1, self.x2) + 1)
                ]
            else:
                # lower left, upper right
                return [
                    (min(self.x1, self.x2) + d, max(self.y1, self.y2) - d)
                    for d in range(0, max(self.x1, self.x2) - min(self.x1, self.x2) + 1)
                ]

        raise ValueError(
            f"Neither horizontal, nor vertical, nor diagonal. x1: {self.x1}, y1: {self.y1}, x2: {self.x2}, y2: {self.y2}"
        )


with open("input5") as f:
    vents = [line.strip() for line in f.readlines()]

vents = [Line(vent) for vent in vents]
vents1 = filter(lambda v: v.is_horizontal() or v.is_vertical(), vents)
diagram = defaultdict(int)
for vent in vents1:
    points = vent.get_points()
    for point in vent.get_points():
        diagram[point] += 1
overlap = [point for point, count in diagram.items() if count >= 2]
print(f"part 1 | solution: {len(overlap)}")

diagram = defaultdict(int)
for vent in vents:
    points = vent.get_points()
    for point in vent.get_points():
        diagram[point] += 1
overlap = [point for point, count in diagram.items() if count >= 2]
print(f"part 2 | solution: {len(overlap)}")
