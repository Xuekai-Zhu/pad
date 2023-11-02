def solution():
    """Jessica is having a sweet tooth and bought 10 chocolate bars, 10 packs of gummy bears, and 20 bags of chocolate chips. Her total rang up to $150. If the cost of a pack of gummy bears is $2 and a bag of chocolate chips costs $5, how much does one chocolate bar cost?"""
    total_items = 40
    total_cost = 150
    gummy_bear_cost = 2
    chocolate_chip_cost = 5
    chocolate_bar_cost = (total_cost - (10 * gummy_bear_cost) - (20 * chocolate_chip_cost)) / 10
    result = chocolate_bar_cost
    return result

print(solution())