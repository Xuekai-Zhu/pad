def solution():
    # Calculate the cost of buying 2 packs of 500 mL milk and individually
    cost_of_2_packs = 2.5
    cost_of_individual = 2 * 1.3

    # Calculate the savings per 2 packs
    savings_per_2_packs = cost_of_individual - cost_of_2_packs

    # Calculate the total savings from buying 10 sets of 2 packs of milk
    total_savings = 10 * savings_per_2_packs
    result = total_savings
    return result

print(solution())