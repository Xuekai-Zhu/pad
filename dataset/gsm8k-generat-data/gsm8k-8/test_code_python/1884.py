def solution():
    # Calculate the weight of 80% of the sandbag
    sand_weight = 0.8 * 250

    # Calculate the weight of the filling material
    filling_weight = 0.4 * sand_weight

    # Calculate the total weight of the sandbag
    total_weight = sand_weight + filling_weight

    result = total_weight
    return result

print(solution())