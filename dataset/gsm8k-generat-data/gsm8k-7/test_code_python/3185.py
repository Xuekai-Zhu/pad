def solution():
    meals_per_day = [20, 40, 50]
    num_restaurants = 3
    num_days_in_week = 7

    # Calculate the total number of meals served per day by all restaurants
    total_meals_per_day = sum(meals_per_day)

    # Calculate the total number of meals served per week by all restaurants
    total_meals_per_week = total_meals_per_day * num_restaurants * num_days_in_week
    result = total_meals_per_week
    return result

print(solution())