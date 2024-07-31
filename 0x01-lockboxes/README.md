# ALX interview-prep questions

## 0x00-pascal_triangle

Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`
- You can assume `n` will be always an integer

## 0x01-lockboxes

Question:

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
  - There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return `True` if all boxes can be opened, else return `False`
