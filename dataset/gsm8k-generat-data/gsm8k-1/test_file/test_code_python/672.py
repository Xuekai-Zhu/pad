def solution():
    """Three people invested $1200 in a joint savings account. After Dylan's investment of 2/5 of the total amount, Frances invested 2/3 of the remaining amount. Skyler's investment accounted for the rest. How much money was Skyler's investment?"""
    total_investment = 1200
    dylan_investment = total_investment * (2/5)
    remaining_investment = total_investment - dylan_investment
    frances_investment = remaining_investment * (2/3)
    skyler_investment = total_investment - dylan_investment - frances_investment
    result = skyler_investment
    return result

print(solution())