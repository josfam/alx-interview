#!/usr/bin/python3

"""Lock boxes interview question solution"""


def canUnlockAll(boxes):
    """Returns True if all boxes can be unlocked, False otherwise"""
    keys_found = set(boxes[0])  # box 0 is unlocked by default
    locked_boxes = {num: box for num, box in enumerate(boxes[1:], start=1)}

    while locked_boxes:
        locked_count = len(locked_boxes)
        locked_copies = {k: v for k, v in locked_boxes.items()}

        for box_number, locked_box in locked_copies.items():
            if box_number not in keys_found:
                continue
            keys_found.update(locked_box)
            del locked_boxes[box_number]  # this box is no longer locked

        if locked_count == len(locked_boxes):  # no boxes were unlocked
            return False
    return True
