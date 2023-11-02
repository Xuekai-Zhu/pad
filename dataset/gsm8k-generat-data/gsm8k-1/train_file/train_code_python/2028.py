def solution():
    """Jeremy buys 3 bags of chips for a party. Stacy and Emily also buy chips for the party. If they need 10 bags of chips total, and Stacy buys 4 bags, how many bags of chips should Emily buy?"""
    jeremy_bags = 3
    stacy_bags = 4
    total_bags = 10
    emily_bags = total_bags - jeremy_bags - stacy_bags
    result = emily_bags
    return result

print(solution())