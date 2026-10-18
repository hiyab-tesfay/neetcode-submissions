class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        res = 0
        l = 0

        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1
            maxLetter = max(count)
            while (r - l + 1) - maxLetter > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
