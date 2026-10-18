class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        
        for i, num in enumerate(nums): 
            if i > 0 and num == nums[i - 1]:
                continue
            s = i + 1
            e = len(nums) - 1
            while s < e:
                if nums[s] + nums[e] + num < 0:
                    s += 1
                elif nums[s] + nums[e] + num > 0:
                    e -= 1
                else:
                    ans.append([num, nums[s], nums[e]])
                    while s<e and nums[s + 1] == nums[e]:
                        s += 1
                    while s<e and nums[e - 1] == nums[e]:
                        e -= 1
                    s += 1
                    e -= 1

        
        return ans