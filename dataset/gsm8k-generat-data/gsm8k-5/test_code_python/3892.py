def solution():
    gina_litter = 2  # Gina collected 2 bags of litter
    neighborhood_litter = 82 * gina_litter  # The neighborhood collected 82 times as much as Gina did
    total_litter = gina_litter + neighborhood_litter  # Calculate the total amount of litter collected
    total_weight = total_litter * 4  # Each bag of litter weighs 4 pounds

    result = total_weight
    return result

print(solution())