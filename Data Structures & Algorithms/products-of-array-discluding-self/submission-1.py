class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        prefix[0] = nums[0]
        postfix = [1] * len(nums)
        postfix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        products = [1] * len(nums)
        products[0] = postfix[1]
        products[-1] = prefix[-2]
        for i in range(1, len(nums)-1):
            products[i] = prefix[i-1] * postfix[i+1]

        return products
