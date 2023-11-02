def solution():
    """A farmer owns a hog that recently gave birth to 6 piglets. If the farmer raises the piglets until they are fully grown, he can sell the fully grown pig for $300. Each piglet must grow for at least 12 months before it is large enough to be sold. It costs the farmer $10 per month to feed each animal until it is sold. If the farmer sells 3 pigs after 12 months, and the remaining 3 pigs after 16 months, how much profit did he earn in total (after deducting the cost of food)?"""
    piglet_cost = 10 * 12
    total_profit = 0

    # Selling the first three pigs after 12 months
    sold_after_12_months = 3
    profit_per_pig_12_months = 300 - piglet_cost
    total_profit += sold_after_12_months * profit_per_pig_12_months

    # Selling the next three pigs after 16 months
    sold_after_16_months = 3
    piglet_cost_for_16_months = 10 * 4 * 3  # 4 extra months for 3 piglets
    profit_per_pig_16_months = 300 - piglet_cost_for_16_months
    total_profit += sold_after_16_months * profit_per_pig_16_months

    result = total_profit
    return result

print(solution())