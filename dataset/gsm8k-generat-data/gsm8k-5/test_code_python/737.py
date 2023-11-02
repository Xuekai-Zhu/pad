def solution():
    packs_of_crayons = 4  # Michael has 4 packs of crayons
    additional_packs = 2  # Michael wants to buy 2 more packs 
    cost_per_pack = 2.5  # Each pack of crayons costs $2.5

    # Calculate the total cost of the packs of crayons Michael will have after the purchase
    total_cost = (packs_of_crayons + additional_packs) * cost_per_pack
    result = total_cost
    return result

print(solution())