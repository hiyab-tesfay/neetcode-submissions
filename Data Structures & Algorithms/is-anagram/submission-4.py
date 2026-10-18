class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS = {}
        mapT = {}

        for i, letter in enumerate(s):
            if letter in mapS:
                mapS[letter] += 1
            else:
                mapS[letter] = 1

        for i, letter in enumerate(t):
            if letter in mapT:
                mapT[letter] += 1
            else:
                mapT[letter] = 1

        for letter in mapS:
            if mapT.get(letter) != mapS[letter]:
                return False

        return True