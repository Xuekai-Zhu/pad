def solution():
    """Jess made 3 different stacks of wooden blocks. The first stack was 7 blocks high, the second stack was 5 block(s) higher than the first, and the final stack was 7 block(s) higher than the second. Jess’ little sister knocked over the entire first tower, in the second tower she left 2 blocks standing, and in the final tower she left 3 blocks standing.  How many blocks in total fell down?"""
    # Define the height of the first tower
    tower1 = 7

    # Define the height of the second tower
    tower2 = tower1 + 5

    # Define the height of the final tower
    tower3 = tower2 + 7

    # Calculate the number of blocks that fell in the first tower
    tower1_fall = tower1

    # Calculate the number of blocks that fell in the second tower
    tower2_fall = tower2 - 2

    # Calculate the number of blocks that fell in the final tower
    tower3_fall = tower3 - 3

    # Calculate the total number of blocks that fell
    total_fall = tower1_fall + tower2_fall + tower3_fall

    # Display the total number of blocks that fell
    result = total_fall
    return result

print(solution())