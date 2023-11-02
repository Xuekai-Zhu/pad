def solution():
    # Calculate the height of each stack
    stack1 = 7
    stack2 = stack1 + 3
    stack3 = stack2 - 6
    stack4 = stack3 + 10

    # Calculate the total number of blocks used
    total_blocks = stack1 + stack2 + stack3 + stack4 + (2 * stack2)

    result = total_blocks
    return result

print(solution())