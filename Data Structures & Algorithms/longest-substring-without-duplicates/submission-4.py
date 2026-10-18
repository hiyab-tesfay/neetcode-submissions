class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        substr = {}  # char -> last seen index
        left = 0
        for i, letter in enumerate(s):
            if letter in substr and substr[letter] >= left:
                left = substr[letter] + 1
            substr[letter] = i
            maxlen = max(maxlen, i - left + 1)
        return maxlen