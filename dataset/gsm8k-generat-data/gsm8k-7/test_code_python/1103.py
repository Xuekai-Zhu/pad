def solution():
    num_centerpieces = 6
    roses_per_centerpiece = 8
    orchids_per_centerpiece = roses_per_centerpiece * 2
    cost_per_flower = 15
    total_cost = 2700

    # Calculate the total number of flowers used in all centerpieces
    total_flowers = num_centerpieces * (roses_per_centerpiece + orchids_per_centerpiece + lilies_per_centerpiece)

    # Calculate the cost of all flowers used
    total_flower_cost = total_flowers * cost_per_flower

    # Calculate the cost of all lilies used
    lilies_cost = total_cost - total_flower_cost

    # Calculate the number of lilies in each centerpiece
    lilies_per_centerpiece = lilies_cost / (num_centerpieces * cost_per_flower)
    result = lilies_per_centerpiece
    return result

print(solution())