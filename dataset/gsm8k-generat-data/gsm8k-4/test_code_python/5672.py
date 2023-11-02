def solution():
    """Pablo made 4 stacks of toy blocks. The first stack was 5 blocks tall. The second stack was 2 blocks taller than the first. The third stack was 5 blocks shorter than the second stack, and the last stack was 5 blocks taller than the third stack. How many toy blocks did Pablo use in all?"""
    # Define the height of the first stack
    stack1 = 5

    # Define the height of the second stack
    stack2 = stack1 + 2

    # Define the height of the third stack
    stack3 = stack2 - 5

    # Define the height of the fourth stack
    stack4 = stack3 + 5

    # Calculate the total number of blocks used
    total_blocks = stack1 + stack2 + stack3 + stack4

    # return the result
    result = total_blocks
    return result

print(solution())