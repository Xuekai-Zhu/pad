def solution():
    
    meals_per_day_rest1 = 20
    meals_per_day_rest2 = 40
    meals_per_day_rest3 = 50
    days_per_week = 7
    total_meals_per_week = (meals_per_day_rest1 + meals_per_day_rest2 +
                            meals_per_day_rest3) * days_per_week
    result = total_meals_per_week
    return result

print(solution())