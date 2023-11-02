def solution():
    # Calculate the total weight of the litter collected
    gina_litter_weight = 2 * 4  # Gina collected 2 bags of litter, each bag weights 4 pounds
    neighborhood_litter_weight = gina_litter_weight * 82  # The neighborhood collected 82 times as much as Gina did by herself
    total_litter_weight = gina_litter_weight + neighborhood_litter_weight

    result = total_litter_weight
    return result

print(solution())