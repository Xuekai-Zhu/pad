def solution():
    
    lunch_meals = 17
    sold_lunch_meals = 12
    dinner_meals = 5
    remaining_lunch_meals = lunch_meals - sold_lunch_meals
    total_dinner_meals = remaining_lunch_meals + dinner_meals
    result = total_dinner_meals
    return result

print(solution())