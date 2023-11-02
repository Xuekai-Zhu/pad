def solution():
    
    crate_weight_limit = 20
    number_of_crates = 15
    crate_capacity = crate_weight_limit * number_of_crates
    nails_weight = 5 * 4
    hammers_weight = 5 * 12
    planks_weight = 10 * 30
    total_weight = nails_weight + hammers_weight + planks_weight
    excess_weight = total_weight - crate_capacity
    result = excess_weight
    return result

print(solution())