def solution():
    """A farmer owns a hog that recently gave birth to 6 piglets. If the farmer raises the piglets until they are fully grown, he can sell the fully grown pig for $300. Each piglet must grow for at least 12 months before it is large enough to be sold. It costs the farmer $10 per month to feed each animal until it is sold. If the farmer sells 3 pigs after 12 months, and the remaining 3 pigs after 16 months, how much profit did he earn in total (after deducting the cost of food)?"""

    piglet_cost = 10 * 12
    fully_grown_profit = 300 - (10 * 12)
    total_profit = (fully_grown_profit * 6) - (piglet_cost * 6)
    profit_after_12_months = (fully_grown_profit * 3) - (piglet_cost * 3)
    profit_after_16_months = (fully_grown_profit * 3) - (piglet_cost * 3)
    total_profit = profit_after_12_months + profit_after_16_months

    result = total_profit
    return result

print(solution())