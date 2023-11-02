def solution():
    # Calculate the total number of green leaves on all 3 plants
    total_leaves = 18 * 3

    # Calculate the number of leaves that turn yellow and fall off on one plant
    lost_leaves = 18/3

    # Calculate the total number of leaves that turn yellow and fall off on all 3 plants
    total_lost_leaves = lost_leaves * 3

    # Calculate the number of green leaves left on all 3 plants
    green_leaves = total_leaves - total_lost_leaves
    result = green_leaves
    return result

print(solution())