def solution():
    """James replaces the coffee for the household. There are 3 other people in the house and everyone drinks 2 cups of coffee a day. It takes .5 ounces of coffee per cup of coffee. If coffee costs $1.25 an ounce, how much does he spend on coffee a week?"""
    people_in_house = 3
    cups_per_day = 2
    ounces_per_cup = 0.5
    price_per_ounce = 1.25
    ounces_per_week = people_in_house * cups_per_day * ounces_per_cup * 7
    cost_per_week = ounces_per_week * price_per_ounce
    result = cost_per_week
    return result

print(solution())