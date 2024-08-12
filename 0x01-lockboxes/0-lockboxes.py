#!/usr/bin/python3
"""
Method to determine if all boxes can be opened
Using prototype: def canUnlockAll(boxes)
"""


def canUnlockAll(boxes):
    """
    Check if boxes can be unlocked
    """
    n = len(boxes)
    opened = set([0])  # Start with the first box opened
    keys = boxes[0]  # Start with keys in the first box

    while keys:
        key = keys.pop()
        if key < n and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == n
