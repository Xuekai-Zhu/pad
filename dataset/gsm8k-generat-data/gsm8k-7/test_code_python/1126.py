def solution():
    type_a_bricks = 40
    type_b_bricks = type_a_bricks / 2
    total_bricks = 150

    # Calculate the total number of type A and type B bricks Mike will use
    total_a_b_bricks = type_a_bricks + type_b_bricks

    # Calculate the number of bricks of other types that Mike will use
    other_bricks = total_bricks - total_a_b_bricks
    result = other_bricks
    return result

print(solution())