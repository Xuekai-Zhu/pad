def solution():
    """Jess made 3 different stacks of wooden blocks. The first stack was 7 blocks high, the second stack was 5 block(s) higher than the first, and the final stack was 7 block(s) higher than the second. Jess’ little sister knocked over the entire first tower, in the second tower she left 2 blocks standing, and in the final tower she left 3 blocks standing. How many blocks in total fell down?"""
    # Define the heights of the three stacks of blocks
    first_stack = 7
    second_stack = first_stack + 5
    final_stack = second_stack + 7

    # Define the number of blocks that fell down in each stack
    first_fell = first_stack
    second_fell = second_stack - 2
    final_fell = final_stack - 3

    # Calculate the total number of blocks that fell down
    total_fell = first_fell + second_fell + final_fell

    # return the result
    result = total_fell
    return result

print(solution())