def solution():
    """In a restaurant, the chef prepared 17 meals to sell for lunch. During lunch, he sold 12 meals. After lunch, the chef prepared another 5 meals for dinner. How many meals does the chef have for dinner, assuming he can use the remaining lunch meals as well?"""
    lunch_meals = 17
    sold_lunch_meals = 12
    dinner_meals = 5
    remaining_lunch_meals = lunch_meals - sold_lunch_meals
    total_dinner_meals = remaining_lunch_meals + dinner_meals
    result = total_dinner_meals
    return result

print(solution())