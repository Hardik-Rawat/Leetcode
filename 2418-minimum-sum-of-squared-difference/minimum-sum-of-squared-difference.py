class Solution:
    def minSumSquareDiff(
        self,
        nums1: List[int],
        nums2: List[int],
        k1: int,
        k2: int
    ) -> int:

        differences = [
            abs(a - b)
            for a, b in zip(nums1, nums2)
        ]

        operations = k1 + k2

        if sum(differences) <= operations:
            return 0

        frequency = [0] * (max(differences) + 1)

        for difference in differences:
            frequency[difference] += 1

        for difference in range(len(frequency) - 1, 0, -1):
            if operations == 0:
                break

            move = min(frequency[difference], operations)

            frequency[difference] -= move
            frequency[difference - 1] += move
            operations -= move

        answer = 0

        for difference, count in enumerate(frequency):
            answer += count * difference * difference

        return answer