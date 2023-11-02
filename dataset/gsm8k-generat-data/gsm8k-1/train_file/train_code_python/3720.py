def solution():
    """Jessica bought 10 chocolate bars, 10 packs of gummy bears, and 20 bags of chocolate chips for a total of $150. If the cost of a pack of gummy bears is $2 and a bag of chocolate chips costs $5, how much does 1 chocolate bar cost?"""
    total_cost = 150
    packs_of_gummy_bears = 10
    cost_of_gummy_bears = 2
    bags_of_chocolate_chips = 20
    cost_of_chocolate_chips = 5
    cost_of_chocolate_bars = (total_cost - (packs_of_gummy_bears * cost_of_gummy_bears) - (bags_of_chocolate_chips * cost_of_chocolate_chips)) / 10
    result = cost_of_chocolate_bars
    return result

print(solution())