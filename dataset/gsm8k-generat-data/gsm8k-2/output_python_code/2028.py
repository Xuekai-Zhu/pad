def solution():
    """Jeremy buys 3 bags of chips for a party. Stacy and Emily also buy chips for the party. If they need 10 bags of chips total, and Stacy buys 4 bags, how many bags of chips should Emily buy?"""
    jeremy_chips = 3
    stacy_chips = 4
    total_chips = 10
    emily_chips = total_chips - jeremy_chips - stacy_chips
    result = emily_chips
    return result

print(solution())