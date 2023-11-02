def solution():
    bag_weight = 250
    filling_density = 1.4  # 40% heavier than sand
    fill_percent = 0.8  # 80% full

    # Calculate the weight of the filling material
    fill_weight = fill_percent * bag_weight
    # Adjust for the density of the filling material
    adjusted_fill_weight = fill_weight * filling_density

    # Calculate the total weight of the bag with filling material
    total_weight = bag_weight + adjusted_fill_weight
    result = total_weight
    return result

print(solution())