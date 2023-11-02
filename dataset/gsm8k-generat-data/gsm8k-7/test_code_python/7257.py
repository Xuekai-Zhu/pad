def solution():
    beef_weight = 20
    pork_weight = beef_weight / 2
    total_weight = beef_weight + pork_weight
    meat_per_meal = 1.5
    num_meals = total_weight / meat_per_meal
    meal_price = 20
    total_sales = num_meals * meal_price
    result = total_sales
    return result

print(solution())