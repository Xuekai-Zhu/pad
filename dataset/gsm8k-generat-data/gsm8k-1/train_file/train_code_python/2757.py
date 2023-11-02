def solution():
    """Mohammad has 80 bags of chips. One quarter of the bags of chips are Doritos. If Mohammad wants to split the bags of Doritos into 4 equal piles, how many bags of Doritos will be in each pile?"""
    total_bags = 80
    doritos_percentage = 0.25
    doritos_bags = total_bags * doritos_percentage
    piles = 4
    bags_per_pile = doritos_bags / piles
    result = bags_per_pile
    return result

print(solution())