def solution():
    
    pounds_to_burn = 5
    calories_in_pound = 3500
    deficit_calories_per_day = 500 
    total_deficit_calories = pounds_to_burn * calories_in_pound
    total_days = total_deficit_calories / deficit_calories_per_day
    result = total_days 
    return result

print(solution())