def solution():
    sand_weight = 250 * 0.8  # Tom fills 80% of the 250 pound sandbag with sand
    filling_weight = sand_weight * 0.4  # The filling material is 40% heavier than sand
    total_weight = sand_weight + filling_weight  # Calculate the total weight of the bag
    result = total_weight
    return result

print(solution())