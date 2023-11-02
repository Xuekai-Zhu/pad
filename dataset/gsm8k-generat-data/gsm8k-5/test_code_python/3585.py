def solution():
    total_meals = 113  # Colt and Curt prepared 113 meals
    additional_meals = 50  # Sole Mart provided 50 more meals
    meals_given_away = 85  # Colt and Curt have already given away 85 meals

    # Calculate how many meals are left to be distributed
    meals_left = total_meals + additional_meals - meals_given_away
    result = meals_left
    return result

print(solution())