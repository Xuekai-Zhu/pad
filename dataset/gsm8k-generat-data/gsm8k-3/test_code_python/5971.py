def solution():
    """Matt can buy key chains in packs of 10 for $20 or in packs of 4 for $12. How much money can he save if he chooses to buy 20 key chains at a lower price?"""
    # Calculate the cost of buying 20 key chains in packs of 10
    packs_of_10 = 20 // 10
    remaining_key_chains = 20 % 10
    cost_10 = packs_of_10 * 20
    if remaining_key_chains > 0:
        cost_10 += 20

    # Calculate the cost of buying 20 key chains in packs of 4
    packs_of_4 = 20 // 4
    remaining_key_chains = 20 % 4
    cost_4 = packs_of_4 * 12
    if remaining_key_chains > 0:
        cost_4 += remaining_key_chains * 3

    # Calculate the amount of money saved by choosing the lower price option
    money_saved = cost_4 - cost_10

    # Display the amount of money saved
    result = money_saved
    return result

print(solution())