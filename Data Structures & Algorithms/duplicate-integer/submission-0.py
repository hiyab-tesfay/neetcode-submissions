class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}

        for index, num in enumerate(nums):
            if num in duplicate:
                return True
            
            duplicate[num] = index

        return False
            