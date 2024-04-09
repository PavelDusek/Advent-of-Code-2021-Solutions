# coding: utf-8
from collections import defaultdict


def get_substitution_rules(line: str) -> dict:
    """Using this diagram:

           TTTTT
          U     V
          U     V
          U     V
           WWWWW
          X     Y
          X     Y
          X     Y
           ZZZZZ

    create substitution rules for abcdefg to TUVWXYZ.
    Uses the fact that len(set(pattern)) maps as follows:
    2 -> 1; 3 -> 7; 4 -> 4; 5 -> 2, 3, 5; 6 -> 0, 6, 9; 7 -> 8.
    """
    numbers = line.split(" ")
    counts = defaultdict(list)
    rules = {}
    for number in numbers:
        counts[len(set(number))].append(number)

    # get T segment: is in 7 but not in 1
    T = set(counts[3][0]) - set(counts[2][0])
    rules["T"] = T.pop()

    # get Z segment: shared in 0, 2, 3, 5, 6, 9, but is not T segment
    Z = set(counts[5][0])
    for number in counts[5] + counts[6]:
        Z = Z & set(number)
    Z = Z - set(rules["T"])
    rules["Z"] = Z.pop()

    # get W segment: shared in 2, 3, 5 but is not T and is not Z segment
    W = set(counts[5][0])
    for number in counts[5]:
        W = W & set(number)
    W = W - set(rules["T"]) - set(rules["Z"])
    rules["W"] = W.pop()

    # get U segment: 4 - 1 - W
    U = set(counts[4][0]) - set(counts[2][0]) - set(rules["W"])
    rules["U"] = U.pop()

    # get Y segment: intersetion of 1 and {0, 6, 9}
    Y = set(counts[2][0])
    for number in counts[6]:
        Y = Y & set(number)
    rules["Y"] = Y.pop()

    # get V segment: 1 - Y
    V = set(counts[2][0]) - set(rules["Y"])
    rules["V"] = V.pop()

    # get X segment: 8 - TZWUYV
    X = (
        set(counts[7][0])
        - set(rules["T"])
        - set(rules["U"])
        - set(rules["V"])
        - set(rules["W"])
        - set(rules["Y"])
        - set(rules["Z"])
    )
    rules["X"] = X.pop()

    return rules


def decode(text: str, rules: dict) -> str:
    codes = {
        "TUVXYZ": "0",
        "VY": "1",
        "TVWXZ": "2",
        "TVWYZ": "3",
        "UVWY": "4",
        "TUWYZ": "5",
        "TUWXYZ": "6",
        "TVY": "7",
        "TUVWXYZ": "8",
        "TUVWYZ": "9",
    }
    digits = text.split(" ")
    # apply substitution rules:
    for rule, segment in rules.items():
        digits = [digit.replace(segment, rule) for digit in digits]
    # sort letters alphabeticaly:
    digits = ["".join(sorted(digit)) for digit in digits]
    # decode:
    digits = [codes.get(digit) for digit in digits]
    return "".join(digits)


def main() -> None:
    # with open("sample8") as f:
    with open("input8") as f:
        signal = [line.strip() for line in f.readlines()]
    patterns = [line.split("|")[0].strip() for line in signal]
    outputs = [line.split("|")[1].strip() for line in signal]
    numbers = []
    for line in outputs:
        numbers.extend([number.strip() for number in line.split(" ")])
    solution = 0
    for number in numbers:
        if len(set(number)) in (2, 3, 4, 7):
            solution += 1
    print(f"part 1 | solution: {solution}")

    solution = 0
    for pattern, output in zip(patterns, outputs):
        rules = get_substitution_rules(line=f"{pattern} {output}")
        number = decode(output, rules)
        solution += int(number)
    print(f"part 2 | solution: {solution}")


if __name__ == "__main__":
    main()
