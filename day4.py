# coding: utf-8
import numpy as np
import re


def is_winning(board: list) -> bool:
    nrows, ncols = board.shape
    # columns
    if ncols in board.sum(axis=0):
        return True
    if nrows in board.sum(axis=1):
        return True
    return False


def search_all_boards(drawn: int, boards: list, marked: list) -> (list, list, list):
    """
    look for the number on boards, and if present, mark it in marked
    return list of indexes of the winning boards
    """
    winning = []
    for index, board in enumerate(boards):
        position = np.where(board == drawn)
        selected_board_marks = marked[index].copy()
        selected_board_marks[position] = 1
        marked[index] = selected_board_marks
        # check if column or row complete
        if is_winning(selected_board_marks):
            winning.append(index)
    return (winning, boards, marked)


def calculate_score(
    winning_index: int, drawn_number: int, boards: list, marked: list
) -> int:
    board_won = boards[winning_index].copy()
    marked_won = marked[winning_index].copy()
    # switch zeros and ones
    marked_won[np.where(marked_won == 1)] = -1
    marked_won[np.where(marked_won == 0)] = 1
    marked_won[np.where(marked_won == -1)] = 0
    return round(np.sum(board_won * marked_won) * drawn_number)


with open("input4") as f:
    data = f.readlines()
drawn_numbers = [int(number) for number in data[0].split(",")]
boards, board = [], []
for line in data[2:]:
    if line == "\n":
        boards.append(np.array(board))
        board = []
    else:
        numbers = re.split(" +", line.strip())
        board.append([int(number) for number in numbers])
# append the last one:
boards.append(np.array(board))

# make a data structure for marked numbers:
marked = [np.zeros(boards[0].shape)] * len(boards)
for drawn in drawn_numbers:
    winning, boards, marked = search_all_boards(drawn, boards, marked)
    if winning:
        for index in winning:
            print(boards[index])
            print(marked[index])
        break
score = calculate_score(winning[0], drawn, boards, marked)
print(f"part 1 | score: {score}")

# make a data structure for marked numbers:
marked = [np.zeros(boards[0].shape)] * len(boards)
for drawn in drawn_numbers:
    winning, boards, marked = search_all_boards(drawn, boards, marked)
    if winning and len(boards) == 1:
        print(boards[winning[0]])
        print(marked[winning[0]])
        break
    if winning and len(boards) > 1:
        for index in winning[::-1]:
            boards.pop(index)
            marked.pop(index)
score = calculate_score(winning[0], drawn, boards, marked)
print(f"part 2 | score: {score}")
