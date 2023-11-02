def solution():
    type_a = 40  # Mike needs at least 40 bricks of type A
    type_b = type_a / 2  # Mike needs half as many bricks of type B
    total_bricks = 150  # Mike needs to use a total of 150 bricks

    # Calculate the number of bricks of other types that Mike will use
    other_bricks = total_bricks - type_a - type_b
    result = other_bricks
    return result

print(solution())