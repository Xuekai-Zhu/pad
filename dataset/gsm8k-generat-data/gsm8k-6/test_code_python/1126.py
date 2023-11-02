def solution():
    # Calculate the number of type A and type B bricks Mike needs
    typeA_bricks = 40
    typeB_bricks = typeA_bricks / 2

    # Calculate the total number of bricks Mike needs
    total_bricks = typeA_bricks + typeB_bricks

    # Calculate the number of bricks that are not type A or type B
    other_bricks = 150 - total_bricks
    result = other_bricks
    return result

print(solution())