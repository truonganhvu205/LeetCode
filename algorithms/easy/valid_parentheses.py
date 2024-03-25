class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != brackets[stack.pop()]:
                return False

        return len(stack) == 0