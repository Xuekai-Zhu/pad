def solution():
    num_half_dozens = 4
    cost_per_crayon = 2
    num_crayons_per_half_dozen = 6

    # Calculate the total number of crayons that Jamal bought
    total_num_crayons = num_half_dozens * num_crayons_per_half_dozen

    # Calculate the total cost of all the crayons
    total_cost = total_num_crayons * cost_per_crayon
    result = total_cost
    return result

print(solution())