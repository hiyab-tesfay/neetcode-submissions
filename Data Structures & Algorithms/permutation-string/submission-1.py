class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashS1 = defaultdict(int)
        for letter in s1:
            hashS1[letter] += 1

        for i in range(len(s2)):
            if s2[i] not in hashS1:
                continue
            hashCheck = defaultdict(int)
            j = i + 1
            hashCheck[s2[i]] = 1
            while j < len(s2) and s2[j] in hashS1:
                hashCheck[s2[j]] += 1
                if hashCheck == hashS1:
                    return True
                j+=1
            if hashCheck == hashS1:
                return True
            else:
                hashCheck = defaultdict(int)
    
        return False
