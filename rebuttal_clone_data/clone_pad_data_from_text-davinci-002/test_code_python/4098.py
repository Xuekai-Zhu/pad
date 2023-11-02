def solution():
    ounces_of_coffee_per_day = 2 * 20
    days_in_week = 5
    reduction = 1/4
    coffee_per_week = ounces_of_coffee_per_day * days_in_week * reduction
    result = coffee_per_week
    return result

print(solution())