def solution():
    # Define the minimum number of type A bricks needed
    type_a_bricks = 40

    # Calculate the minimum number of type B bricks needed
    type_b_bricks = type_a_bricks / 2

    # Calculate the total number of bricks needed
    total_bricks = 150

    # Calculate the total number of type A and type B bricks used
    total_a_and_b_bricks = type_a_bricks + type_b_bricks

    # Calculate the number of bricks of other types used
    other_bricks = total_bricks - total_a_and_b_bricks
    result = other_bricks
    return result

print(solution())