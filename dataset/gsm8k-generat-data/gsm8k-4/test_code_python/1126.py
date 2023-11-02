def solution():
    """Mike is building a bridge out of LEGO blocks. To be successful he needs at least 40 bricks of type A, and half that many of type B. In total, he needs to use 150 bricks. How many bricks of other types than mentioned is he going to use?"""
    # Define the minimum number of type A bricks and calculate the minimum number of type B bricks
    type_A_min = 40
    type_B_min = type_A_min / 2

    # Calculate the total number of mentioned bricks
    total_mentioned = type_A_min + type_B_min

    # Calculate the number of bricks of other types
    other_bricks = 150 - total_mentioned

    # Return the result
    result = other_bricks
    return result

print(solution())