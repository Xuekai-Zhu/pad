def solution():
    """Matt can buy key chains in packs of 10 for $20 or in packs of 4 for $12. How much money can he save if he chooses to buy 20 key chains at a lower price?"""
    # Calculate the cost of buying 20 key chains in packs of 10
    packs_of_10 = 2  # 20 key chains / 10 key chains per pack
    cost_packs_of_10 = packs_of_10 * 20
    
    # Calculate the cost of buying 20 key chains in packs of 4
    packs_of_4 = 5  # 20 key chains / 4 key chains per pack
    cost_packs_of_4 = packs_of_4 * 12
    
    # Calculate the amount saved by choosing the lower price
    amount_saved = cost_packs_of_4 - cost_packs_of_10
    
    result = amount_saved
    return result

print(solution())