# 0x07. Rotate 2D Matrix

## Project Overview
In this project, we implement an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. The challenge is to modify the matrix in place without using any extra space for another matrix.

## Key Concepts:
- **Matrix Transposition**: Converting rows to columns.
- **In-place Operations**: Operations that do not use extra memory.
- **Row Reversal**: Reversing rows after transposing the matrix.

## Problem Statement:
Given an `n x n` matrix, rotate it 90 degrees clockwise in place.

### Example:

Input: 1 2 3 4 5 6 7 8 9

Output: 7 4 1 8 5 2 9 6 3


## Approach:
1. **Transpose the matrix** by swapping the elements along the diagonal.
2. **Reverse each row** to complete the 90-degree rotation.

## Usage:
1. Implement the function in `0-rotate_2d_matrix.py`.
2. Run `main_0.py` to test the function.

### Example Test:
$ ./main_0.py [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

## Requirements:
- Python 3.8.10
- No external libraries or imports are allowed.
- The solution must modify the matrix in place.

## Files:
- `0-rotate_2d_matrix.py`: Contains the `rotate_2d_matrix` function.
- `main_0.py`: Test file to validate the solution.
