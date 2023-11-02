def solution():
    
    calories_to_lose_one_pound = 4000
    pounds_to_lose = 10
    total_calories_to_lose = calories_to_lose_one_pound * pounds_to_lose
    daily_calorie_deficit = 500  
    days_to_lose_weight = total_calories_to_lose / (daily_calorie_deficit)
    result = days_to_lose_weight
    return result

print(solution())