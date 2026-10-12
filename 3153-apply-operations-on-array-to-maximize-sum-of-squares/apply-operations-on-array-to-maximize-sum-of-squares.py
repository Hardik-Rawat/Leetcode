class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 31

        # Count how many times each bit appears
        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    count[bit] += 1

        answer = 0

        # Create k maximum possible numbers
        for _ in range(k):
            current = 0

            for bit in range(31):
                if count[bit] > 0:
                    current |= (1 << bit)
                    count[bit] -= 1

            answer = (answer + current * current) % MOD

        return answer