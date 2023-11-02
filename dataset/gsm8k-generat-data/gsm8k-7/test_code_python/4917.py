def solution():
    total_weight = 540
    crate_weight = 30
    crate_cost = 1.5

    # Calculate the total number of crates needed
    num_crates = total_weight / crate_weight

    # Calculate the total cost of shipping the crates
    total_cost = num_crates * crate_cost
    result = total_cost
    return result

print(solution())