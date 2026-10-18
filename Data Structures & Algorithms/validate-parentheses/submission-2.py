class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"}": "{", ")": "(", "]": "["}
        stack = []

        for i in s:
            if i in valid and stack:
                pop = stack.pop()
                if pop != valid[i]:
                    return False
                continue
            stack.append(i)

        return not stack