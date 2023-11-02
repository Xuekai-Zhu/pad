def solution():
    # Calculate the cost of buying 20 key chains in packs of 10
    cost_pack_10 = 20  # $20 for a pack of 10 key chains
    cost_20_pack_10 = (20 // 10) * cost_pack_10  # cost of buying 20 key chains in packs of 10

    # Calculate the cost of buying 20 key chains in packs of 4
    cost_pack_4 = 12  # $12 for a pack of 4 key chains
    cost_20_pack_4 = (20 // 4) * cost_pack_4  # cost of buying 20 key chains in packs of 4

    # Calculate the amount of money saved by choosing the lower price option
    amount_saved = cost_20_pack_10 - cost_20_pack_4
    result = amount_saved
    return result

print(solution())