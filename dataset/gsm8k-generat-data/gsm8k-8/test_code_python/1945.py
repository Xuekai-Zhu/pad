def solution():
    # Calculate the total weight of the fruit Diego is already carrying
    current_weight = 3

    # Calculate the remaining weight Diego has in his bookbag
    remaining_weight = 20 - current_weight

    # Calculate the weight of one pound of apples
    apple_weight = remaining_weight / 4

    result = apple_weight
    return result

print(solution())