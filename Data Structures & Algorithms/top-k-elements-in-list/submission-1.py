class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)

        for i in nums:
            frequencies[i] += 1

        return heapq.nlargest(k, frequencies, key=frequencies.get)