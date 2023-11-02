def solution():
    
    dogs = 3
    daily_food_per_dog = 0.5 * 2
    weekly_food_per_dog = daily_food_per_dog * 7
    total_weekly_food = weekly_food_per_dog * dogs
    remaining_food = 30 - total_weekly_food
    result = remaining_food
    return result

print(solution())