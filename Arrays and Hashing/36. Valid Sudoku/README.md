# 36. Valid Sudoku 🎯

- Difficulty: ![Medium](https://img.shields.io/badge/Medium-ffc926)
- Link: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

## Problem Statement 📜

Welcome to the world of Sudoku validation! Your mission, should you choose to accept it, is to determine whether a given 9x9 Sudoku board is valid. A valid board is one where each column, each row, and each of the nine 3x3 sub-grids that compose the grid contain distinct numbers from 1 to 9. An empty cell is indicated by the character `'.'`.

Dive into this puzzling journey as you unveil the validity of a Sudoku board! 🌟🧩

## Intuition 🤔

To validate a Sudoku board, you must ensure that each row, column, and 3x3 sub-grid contains only distinct numbers from 1 to 9. One approach involves using hash sets to track the numbers encountered in each row, column, and sub-grid. Traverse the board and populate the hash sets, ensuring no repetition.

## Approach 🛤️

1. Create hash sets to track numbers in rows, columns, and sub-grids.
2. Traverse the board using nested loops for rows and columns.
   - For each cell, check if it's empty (`'.'`).
   - If not empty, check if the number exists in the corresponding row, column, or sub-grid hash set.
   - If it does, return `False`.
   - Otherwise, add the number to the respective hash sets.
3. If the entire board is validated, return `True`.

## Complexity ⏳

- Time Complexity: **O(1)**

  - The 9x9 board size is fixed, resulting in a constant number of iterations.

- Space Complexity: **O(1)**
  - The hash sets and other data structures have a fixed size regardless of the input size.

## Code 🚀

[Python Code](36.%20Valid%20Sudoku.py)

Feel free to explore alternative strategies and enhancements. If you encounter uncertainties or seek further guidance, don't hesitate to reach out. Best wishes on your Sudoku validation journey! 🌟💻
