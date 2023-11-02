def solution():
    
    pounds_to_lose = 5
    calories_per_pound = 3500
    total_calories_to_lose = pounds_to_lose * calories_per_pound
    daily_calorie_deficit = 500
    calories_burned_per_day = 2500
    calories_consumed_per_day = 2000
    calories_deficit_per_day = calories_burned_per_day - calories_consumed_per_day
    days_to_lose_weight = total_calories_to_lose/(calories_deficit_per_day)
    result = days_to_lose_weight
    return result

print(solution())