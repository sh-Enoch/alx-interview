#!/usr/bin/python3
"""Determine if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Unlock boxes."""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    unlocked_boxes = set([0])

    for box_idx, box in enumerate(boxes):
        if box_idx in unlocked_boxes:
            unlocked_boxes.update(box)

    return len(unlocked_boxes) == len(boxes)
