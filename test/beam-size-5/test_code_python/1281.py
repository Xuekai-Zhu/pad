def solution():
    
    total_meals = 1360
    friday_meals = 64
    saturday_meals = 30
    sunday_meals = 48
    remaining_meals = total_meals - (friday_meals + saturday_meals + sunday_meals)
    result = remaining_meals
    return result

print(solution())