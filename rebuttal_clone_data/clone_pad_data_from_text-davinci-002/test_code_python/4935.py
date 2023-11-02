def solution():
    desired_weight_loss = 5
    daily_calorie_deficit = 500
    calories_per_day = 2000
    calories_burned_per_day = 2500
    calories_in_a_pound = 3500
    days_to_lose_weight = (desired_weight_loss * calories_in_a_pound) / (calories_burned_per_day - daily_calorie_deficit)
    result = days_to_lose_weight
    return result

print(solution())