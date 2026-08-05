class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        bracket_dict = {')': '(', '}':'{', ']':'['}
        for char in string:
            if char in bracket_dict.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                closing_bracket = bracket_dict.get(char)
                last = stack.pop()
                if closing_bracket != last:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False