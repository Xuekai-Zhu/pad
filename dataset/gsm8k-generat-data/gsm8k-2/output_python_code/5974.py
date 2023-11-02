def solution():
    """A cup of dog food weighs 1/4 of a pound. If Mike has 2 dogs that each eat 6 cups of dog food twice a day how many 20 pound bags of dog food does he need to buy a month?"""
    dogs = 2
    cups_per_day = 6 * 2
    pounds_per_cup = 1/4
    pounds_per_day = cups_per_day * pounds_per_cup
    pounds_per_month = pounds_per_day * 30
    bags_per_month = pounds_per_month / 20
    result = bags_per_month
    return result

print(solution())