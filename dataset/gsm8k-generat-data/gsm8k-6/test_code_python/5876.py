def solution():
    # Calculate the number of blocks used in each stack
    stack1 = 7
    stack2 = stack1 + 3
    stack3 = stack2 - 6
    stack4 = stack3 + 10
    stack5 = 2 * stack2

    # Calculate the total number of blocks used
    total_blocks = stack1 + stack2 + stack3 + stack4 + stack5
    result = total_blocks
    return result

print(solution())