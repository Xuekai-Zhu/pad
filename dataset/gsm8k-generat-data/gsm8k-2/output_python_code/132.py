def solution():
    """James buys 5 packs of beef that are 4 pounds each. The price of beef is $5.50 per pound. How much did he pay?"""
    packs = 5
    weight_per_pack = 4
    price_per_pound = 5.5
    total_weight = packs * weight_per_pack
    total_cost = total_weight * price_per_pound
    result = total_cost
    return result

print(solution())