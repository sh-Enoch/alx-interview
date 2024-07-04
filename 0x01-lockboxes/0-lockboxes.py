#!/usr/bin/python3
"""Determine if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Unlock boxes."""
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for j in range(i, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
            if boxes_checked is False:
                return boxes_checked
    return True
