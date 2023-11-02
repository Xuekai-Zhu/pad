def solution():
    # Calculate the cost of buying 2 packs together
    pack_cost = 2.50 / 2
    # Calculate the cost of buying 1 pack individually
    single_pack_cost = 1.30
    # Calculate the savings per 2 packs
    savings_per_pack = (2 * single_pack_cost) - pack_cost
    # Calculate the total savings for 10 sets of 2 packs
    total_savings = 10 * savings_per_pack
    result = total_savings
    return result

print(solution())