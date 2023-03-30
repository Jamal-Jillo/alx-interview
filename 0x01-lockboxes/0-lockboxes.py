#!/usr/bin/python3
"""0-lockboxes.py."""


def canUnlockAll(boxes):
    """Functions that determines if all the boxes can be opened."""
    n = len(boxes)  # number of boxes
    unlocked = [False] * n  # list of unlocked boxes
    unlocked[0] = True  # first box is unlocked by default
    stack = [0]  # start with first box
    while stack:  # while stack is not empty
        box = stack.pop()  # get the first box in the stack and save it in box
        for key in boxes[box]:  # for each key in the box
            if key < n and not unlocked[key]:  # if the key is not in the list
                # of unlocked boxes
                unlocked[key] = True
                stack.append(key)
    return all(unlocked)
