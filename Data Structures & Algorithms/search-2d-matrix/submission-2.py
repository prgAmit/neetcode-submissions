class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: 
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        # Correct row selection
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        # If no valid row found
        if not (top <= bot):
            return False

        row = (top + bot) // 2

        # Binary search inside the row
        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
            else:
                return True

        return False
