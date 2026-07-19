class Solution:
    def maxPeopleVisible(self, arr):
        n = len(arr)
        visible = [1] * n  # Count self

        # Visible on the left
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                visible[i] += 1
                stack.pop()
            if stack:
                visible[i] += 1
            stack.append(i)

        # Visible on the right
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                visible[i] += 1
                stack.pop()
            if stack:
                visible[i] += 1
            stack.append(i)

        return max(visible)