def solution():
    lunch_meals = 17  # Chef prepared 17 meals for lunch
    sold_lunch_meals = 12  # Chef sold 12 meals during lunch
    remaining_lunch_meals = lunch_meals - sold_lunch_meals  # Chef has these meals left to use for dinner
    dinner_meals = remaining_lunch_meals + 5  # Chef prepared 5 more meals for dinner
    result = dinner_meals
    return result

print(solution())