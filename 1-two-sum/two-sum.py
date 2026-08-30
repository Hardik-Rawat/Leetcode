class Solution(object):
    def twoSum(self, nums, target):
        'Hardik'
        prevMap={}

        for i, n in enumerate(nums):
            diff= target-n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n]=i
        return
