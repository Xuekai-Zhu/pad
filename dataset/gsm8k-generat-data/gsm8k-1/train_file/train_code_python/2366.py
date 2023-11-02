def solution():
    """In a restaurant, the chef prepared 17 meals to sell for lunch. During lunch, he sold 12 meals. After lunch, the chef prepared another 5 meals for dinner. How many meals does the chef have for dinner, assuming he can use the remaining lunch meals as well?"""
    lunch_prepared = 17
    lunch_sold = 12
    dinner_prepared = 5
    remaining_meals = lunch_prepared - lunch_sold
    total_dinner_meals = remaining_meals + dinner_prepared
    result = total_dinner_meals
    return result

print(solution())