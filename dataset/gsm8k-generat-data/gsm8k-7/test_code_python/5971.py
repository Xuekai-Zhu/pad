def solution():
    # If Matt buys in packs of 10
    num_packs_of_10 = 2
    cost_per_pack_of_10 = 20
    total_cost_10 = num_packs_of_10 * cost_per_pack_of_10

    # If Matt buys in packs of 4
    num_packs_of_4 = 5
    cost_per_pack_of_4 = 12
    total_cost_4 = num_packs_of_4 * cost_per_pack_of_4

    # Calculate savings
    total_cost = 40
    total_savings = total_cost - min(total_cost_10, total_cost_4)
    result = total_savings
    return result

print(solution())