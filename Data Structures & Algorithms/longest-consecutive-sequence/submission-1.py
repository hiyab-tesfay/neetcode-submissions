class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set(nums)
        seq = defaultdict(set)
        
        for i in elems:
            if (i-1) not in elems:
                seq[i].add(i)
        
        for i in seq:
            nextValue = i+1
            while nextValue in elems:
                seq[i].add(nextValue)
                nextValue += 1
        
        count = 0
        for i in seq:
            count = len(seq[i]) if len(seq[i]) > count else count
        
        return count
