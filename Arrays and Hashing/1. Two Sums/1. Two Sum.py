class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumsDict = {}

        for index, value in enumerate(nums):
            diff = target - value
            if sumsDict.get(diff, -1) != -1:
                return [sumsDict[diff], index]
            sumsDict[value] = index
