def solution():
    num_cans_of_soda = 6
    weight_per_can_of_soda = 12  # ounces
    weight_per_empty_can = 2  # ounces
    num_empty_cans = 2

    # Calculate the total weight of the soda
    total_soda_weight = num_cans_of_soda * weight_per_can_of_soda

    # Calculate the total weight of all empty cans
    total_empty_can_weight = (num_cans_of_soda + num_empty_cans) * weight_per_empty_can

    # Calculate the total weight that the bridge must support
    total_weight = total_soda_weight + total_empty_can_weight
    result = total_weight
    return result

print(solution())