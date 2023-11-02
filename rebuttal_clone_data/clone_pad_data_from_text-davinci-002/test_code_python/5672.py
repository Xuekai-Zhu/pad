def solution():
    stack1 = 5
    stack2 = stack1 + 2
    stack3 = stack2 - 5
    stack4 = stack3 + 5
    total_blocks = stack1 + stack2 + stack3 + stack4
    result = total_blocks
    return result

print(solution())