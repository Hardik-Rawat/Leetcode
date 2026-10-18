from math import comb
from typing import List
import sys


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        sys.setrecursionlimit(5000)
        MOD = 10**9 + 7

        def count_ways(values):
            if len(values) <= 2:
                return 1

            root = values[0]

            left = [value for value in values[1:] if value < root]
            right = [value for value in values[1:] if value > root]

            left_ways = count_ways(left)
            right_ways = count_ways(right)

            interleavings = comb(
                len(left) + len(right),
                len(left)
            )

            return (
                interleavings * left_ways * right_ways
            ) % MOD

        return (count_ways(nums) - 1) % MOD