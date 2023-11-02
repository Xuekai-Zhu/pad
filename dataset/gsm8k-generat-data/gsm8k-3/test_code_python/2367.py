def solution():
    """In a restaurant, the chef prepared 17 meals to sell for lunch. During lunch, he sold 12 meals. After lunch, the chef prepared another 5 meals for dinner. How many meals does the chef have for dinner, assuming he can use the remaining lunch meals as well?"""
    # Define the number of meals prepared for lunch and sold during lunch
    lunch_prepared = 17
    lunch_sold = 12

    # Define the number of meals prepared for dinner
    dinner_prepared = 5

    # Calculate the remaining meals available for dinner
    remaining_meals = lunch_prepared - lunch_sold + dinner_prepared

    # Display the number of meals available for dinner
    result = remaining_meals
    return result

print(solution())