def solution():
    dogs = 4
    meals_per_day = 2
    food_per_meal = 250
    total_food = dogs * meals_per_day * food_per_meal
    food_weight = 50 * 2
    food_days = food_weight / total_food
    result = food_days
    return result

print(solution())