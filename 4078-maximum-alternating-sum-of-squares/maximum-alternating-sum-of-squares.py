class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = [num **2 for num in nums]
        squares.sort()

        middle = len(nums)//2

        return sum(squares[middle:]) - sum(squares[:middle])