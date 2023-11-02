def solution():
    """Angie bought 3 lbs. of coffee at the store today. Each lb. of coffee will brew about 40 cups of coffee. Angie drinks 3 cups of coffee every day. How many days will this coffee last her?"""
    coffee_weight = 3
    cups_per_pound = 40
    total_cups = coffee_weight * cups_per_pound
    cups_per_day = 3
    days_of_coffee = total_cups / cups_per_day
    result = days_of_coffee
    return result

print(solution())