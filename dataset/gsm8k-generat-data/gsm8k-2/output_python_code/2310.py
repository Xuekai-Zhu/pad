def solution():
    """Melody has three dogs. Each dog eats 1/2 of a pound of dog food twice a day. If Melody bought 30 pounds of dog food, how many pounds of dog food are left after a week?"""
    dogs = 3
    daily_food_per_dog = 0.5 * 2
    weekly_food_per_dog = daily_food_per_dog * 7
    total_weekly_food = dogs * weekly_food_per_dog
    remaining_food = 30 - total_weekly_food
    result = remaining_food
    return result

print(solution())