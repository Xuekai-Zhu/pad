def solution():
    """In a restaurant, the chef prepared 17 meals to sell for lunch. During lunch, he sold 12 meals. After lunch, the chef prepared another 5 meals for dinner. How many meals does the chef have for dinner, assuming he can use the remaining lunch meals as well?"""
    # Define the number of lunch meals prepared
    lunch_meals = 17

    # Calculate the number of lunch meals remaining
    lunch_meals_remaining = lunch_meals - 12

    # Calculate the total number of meals for dinner
    dinner_meals = lunch_meals_remaining + 5

    # return the result
    result = dinner_meals
    return result

print(solution())