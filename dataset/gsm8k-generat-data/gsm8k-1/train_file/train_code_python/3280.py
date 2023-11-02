def solution():
    """Jaylen’s dog eats 1 cup of dog food in the morning and 1 cup of dog food in the evening. If she buys a bag that has 32 cups of dog food, how many days can she feed her dog with it?"""
    cups_per_day = 2 # 1 cup in the morning and 1 cup in the evening
    total_cups = 32
    days_of_food = total_cups / cups_per_day
    result = days_of_food
    return result

print(solution())