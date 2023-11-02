def solution():
    # Define the variables
    num_centerpieces = 6
    roses_per_centerpiece = 8
    orchids_per_centerpiece = 2 * roses_per_centerpiece
    total_flowers_per_centerpiece = roses_per_centerpiece + orchids_per_centerpiece + lilies_per_centerpiece
    cost_per_flower = 15
    total_cost = 2700

    # Use algebra to solve for the number of lilies in each centerpiece
    lilies_per_centerpiece = (total_cost - num_centerpieces * (roses_per_centerpiece + orchids_per_centerpiece) * cost_per_flower) / (num_centerpieces * lilies_per_centerpiece * cost_per_flower)

    result = lilies_per_centerpiece
    return result

print(solution())