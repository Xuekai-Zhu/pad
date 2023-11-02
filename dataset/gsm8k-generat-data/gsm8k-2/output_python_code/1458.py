def solution():
    """James replaces the coffee for the household. There are 3 other people in the house and everyone drinks 2 cups of coffee a day. It takes .5 ounces of coffee per cup of coffee. If coffee costs $1.25 an ounce, how much does he spend on coffee a week?"""
    num_people = 4
    cups_per_day = 2
    ounces_per_cup = 0.5
    cost_per_ounce = 1.25
    total_cups_per_week = num_people * cups_per_day * 7
    total_ounces_per_week = total_cups_per_week * ounces_per_cup
    total_cost_per_week = total_ounces_per_week * cost_per_ounce
    result = total_cost_per_week
    return result

print(solution())