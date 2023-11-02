def solution():
    """Thomas made 4 stacks of wooden blocks. The first stack was 7 blocks tall. 
    The second stack was 3 blocks taller than the first. The third stack was 6 blocks shorter than the second stack, 
    and the fourth stack was 10 blocks taller than the third stack. If the fifth stack has twice 
    as many blocks as the second stack, how many blocks did Thomas use in all?"""
    
    # Define the first stack height
    stack1 = 7

    # Define the second stack height
    stack2 = stack1 + 3

    # Define the third stack height
    stack3 = stack2 - 6

    # Define the fourth stack height
    stack4 = stack3 + 10

    # Define the fifth stack height
    stack5 = stack2 * 2

    # Calculate the total number of blocks used
    total_blocks = stack1 + stack2 + stack3 + stack4 + stack5

    result = total_blocks
    return result

print(solution())