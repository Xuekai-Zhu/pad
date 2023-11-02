def solution():
    weight_per_can = 12  # Each can has 12 ounces of soda
    weight_empty_can = 2  # Each can weighs 2 ounces when empty
    num_cans = 6 + 2  # John has 6 full cans and 2 empty cans
    total_weight = num_cans * (weight_per_can + weight_empty_can)  # Calculate the total weight to be supported
    result = total_weight
    return result

print(solution())