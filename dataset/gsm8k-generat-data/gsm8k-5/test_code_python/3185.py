def solution():
    meals_per_day = [20, 40, 50]  # Number of meals served by each restaurant per day
    days_per_week = 7  # Number of days in a week
    total_meals_per_week = sum(meals_per_day) * days_per_week  # Total number of meals served per week by all restaurants

    result = total_meals_per_week
    return result

print(solution())