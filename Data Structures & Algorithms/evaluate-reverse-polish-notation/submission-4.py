class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+', '-', '*', '/')
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(int(left / right))
        if len(stack) > 0:
            return int(stack[0])
        return int(tokens[0])