def solution():
    
    lunch_prepared = 17
    lunch_sold = 12
    dinner_prepared = 5
    remaining_meals = lunch_prepared - lunch_sold
    total_dinner_meals = remaining_meals + dinner_prepared
    result = total_dinner_meals
    return result

print(solution())