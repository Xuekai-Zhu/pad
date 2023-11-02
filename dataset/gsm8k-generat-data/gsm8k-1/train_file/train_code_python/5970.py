def solution():
    """Matt can buy key chains in packs of 10 for $20 or in packs of 4 for $12. How much money can he save if he chooses to buy 20 key chains at a lower price?"""
    # Calculate cost per key chain in both cases
    cost_per_keychain_10 = 20 / 10
    cost_per_keychain_4 = 12 / 4
    
    # Calculate total cost for buying 20 key chains in both cases
    total_cost_10 = cost_per_keychain_10 * 20
    total_cost_4 = cost_per_keychain_4 * 20
    
    # Calculate the amount saved by choosing the lower price option
    amount_saved = total_cost_10 - total_cost_4
    
    result = amount_saved
    return result

print(solution())