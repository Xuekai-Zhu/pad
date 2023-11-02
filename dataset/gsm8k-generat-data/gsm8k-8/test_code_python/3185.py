def solution():
    meals_per_day = [20, 40, 50] # meals served in each restaurant per day
    days_per_week = 7 # number of days in a week

    total_meals = sum(meals_per_day) * days_per_week # multiply total meals per day by days per week

    result = total_meals
    return result

print(solution())