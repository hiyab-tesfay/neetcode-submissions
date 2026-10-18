class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        j = len(heights) - 1
        i = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j-i)
            maxA = area if area > maxA else maxA
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return maxA
            