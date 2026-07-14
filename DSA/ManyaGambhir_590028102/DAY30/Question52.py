def insertBottom(stack, x):
    if not stack:
        stack.append(x)
        return

    temp = stack.pop()
    insertBottom(stack, x)
    stack.append(temp)


stack = list(map(int, input().split()))
x = int(input())

insertBottom(stack, x)
print(stack)