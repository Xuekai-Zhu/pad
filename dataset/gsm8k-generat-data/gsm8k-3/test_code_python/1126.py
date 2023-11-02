def solution():
    """Mike is building a bridge out of LEGO blocks. To be successful he needs at least 40 bricks of type A, and half that many of type B. In total, he needs to use 150 bricks. How many bricks of other types than mentioned is he going to use?"""
    # Define the number of bricks of type A
    bricks_A = 40

    # Calculate the number of bricks of type B
    bricks_B = bricks_A / 2

    # Calculate the total number of bricks used
    total_bricks = 150

    # Calculate the number of bricks of other types used
    other_bricks = total_bricks - bricks_A - bricks_B

    # Display the number of bricks of other types used
    result = other_bricks
    return result

print(solution())