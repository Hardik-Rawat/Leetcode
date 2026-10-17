class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            return sum(int(digit) for digit in str(x))

        sorted_nums = sorted(
            nums,
            key=lambda x: (digit_sum(x), x)
        )

        target_index = {
            value: index
            for index, value in enumerate(sorted_nums)
        }

        visited = [False] * len(nums)
        swaps = 0

        for i in range(len(nums)):
            if visited[i]:
                continue

            cycle_length = 0
            j = i

            while not visited[j]:
                visited[j] = True
                cycle_length += 1
                j = target_index[nums[j]]

            swaps += cycle_length - 1

        return swaps