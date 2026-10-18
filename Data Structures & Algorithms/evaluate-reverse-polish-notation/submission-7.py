import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = tokens[0]
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }
        for i in tokens:
            if i in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(operators[i](num2, num1))
                continue
            stack.append(int(i))
        
        return int(stack[0])