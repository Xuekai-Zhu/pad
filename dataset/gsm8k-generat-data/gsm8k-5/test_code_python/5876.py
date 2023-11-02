def solution():
    # Calculate the number of blocks in the first stack
    stack_1 = 7

    # Calculate the number of blocks in the second stack
    stack_2 = stack_1 + 3

    # Calculate the number of blocks in the third stack
    stack_3 = stack_2 - 6

    # Calculate the number of blocks in the fourth stack
    stack_4 = stack_3 + 10

    # Calculate the number of blocks in the fifth stack
    stack_5 = 2 * stack_2

    # Calculate the total number of blocks Thomas used
    total_blocks = stack_1 + stack_2 + stack_3 + stack_4 + stack_5
    result = total_blocks
    return result

print(solution())