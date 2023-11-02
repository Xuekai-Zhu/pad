def solution():
    crate_weight = 4
    carton_weight = 3
    number_of_crates = 12
    number_of_cartons = 16
    total_weight_crates = crate_weight * number_of_crates
    total_weight_cartons = carton_weight * number_of_cartons
    total_weight = total_weight_crates + total_weight_cartons
    result = total_weight
    return result

print(solution())