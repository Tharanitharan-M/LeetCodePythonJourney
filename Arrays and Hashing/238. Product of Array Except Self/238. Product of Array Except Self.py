class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answers = [1] * length

        prefix = 1
        for index in range(length):
            answers[index] = prefix
            prefix *= nums[index]

        postfix = 1
        for index in range(length - 1, -1, -1):
            answers[index] *= postfix
            postfix *= nums[index]

        return answers
