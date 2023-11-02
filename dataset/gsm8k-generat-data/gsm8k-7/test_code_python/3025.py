def solution():
    crate_weight = 4
    carton_weight = 3
    num_crates = 12
    num_cartons = 16

    # Calculate the total weight of all crates
    total_crate_weight = crate_weight * num_crates

    # Calculate the total weight of all cartons
    total_carton_weight = carton_weight * num_cartons

    # Calculate the total weight of all vegetables
    total_weight = total_crate_weight + total_carton_weight
    result = total_weight
    return result

print(solution())