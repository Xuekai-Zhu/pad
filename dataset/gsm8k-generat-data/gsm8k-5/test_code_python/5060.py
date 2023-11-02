def solution():
    # Cost of 2 packs of 500 mL milk
    cost_2_packs = 2.50

    # Cost of one pack of 500 mL milk
    cost_1_pack = 1.30

    # Cost of 2 packs of 500 mL milk when bought individually
    cost_2_packs_individual = 2 * cost_1_pack

    # Calculate the savings from buying 2 packs together
    savings_per_2_packs = cost_2_packs_individual - cost_2_packs

    # Total savings from buying 10 sets of 2 packs
    total_savings = 10 * 2 * savings_per_2_packs
    result = total_savings
    return result

print(solution())