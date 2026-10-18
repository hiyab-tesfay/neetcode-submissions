class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in exist:
                return [exist[difference], i]

            exist[num] = i
        
        return None