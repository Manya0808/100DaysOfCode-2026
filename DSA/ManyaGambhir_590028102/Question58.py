class Solution:
    def postfixToPrefix(self, s):
        stack = []

        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(ch + op2 + op1)

        return stack[-1]