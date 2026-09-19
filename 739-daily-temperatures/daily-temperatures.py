class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0]* len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):
                while stack and temperature > stack[-1][0]:
                    prevT , prevI = stack.pop()
                    res[prevI] = (index - prevI)
                stack.append([temperature, index])
        return res