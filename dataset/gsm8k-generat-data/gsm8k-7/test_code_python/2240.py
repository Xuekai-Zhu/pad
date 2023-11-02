def solution():
    num_frozen_yogurt = 5
    num_chewing_gum = 2
    num_jumbo_shrimp = 5

    total_cost = 55.0
    jumbo_shrimp_price = 5.0

    # Calculate the cost of all the jumbo shrimp
    jumbo_shrimp_cost = num_jumbo_shrimp * jumbo_shrimp_price

    # Subtract the cost of the jumbo shrimp from the total cost to get the cost of the frozen yogurt and chewing gum
    yogurt_gum_cost = total_cost - jumbo_shrimp_cost

    # Calculate the cost of two packs of chewing gum
    gum_cost = (num_chewing_gum / 2) * yogurt_gum_cost / num_frozen_yogurt

    # Calculate the cost of one pint of frozen yogurt
    yogurt_cost = (yogurt_gum_cost - gum_cost) / num_frozen_yogurt
    result = yogurt_cost
    return result

print(solution())