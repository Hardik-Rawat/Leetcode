class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        top = 0
        bottom = rows - 1

        # First binary search: find the correct row
        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bottom = row - 1

            else:
                break

        # No possible row was found
        if top > bottom:
            return False

        row = (top + bottom) // 2

        left = 0
        right = columns - 1

        # Second binary search: search inside the row
        while left <= right:
            middle = (left + right) // 2

            if matrix[row][middle] > target:
                right = middle - 1

            elif matrix[row][middle] < target:
                left = middle + 1

            else:
                return True

        return False