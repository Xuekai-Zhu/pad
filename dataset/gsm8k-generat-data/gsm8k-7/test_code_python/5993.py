def solution():
    daily_calories_eaten = 1800
    daily_calories_burned = 2300
    calories_needed_to_lose_1lb = 4000
    pounds_to_lose = 10

    # Calculate the daily calorie deficit
    daily_calorie_deficit = daily_calories_burned - daily_calories_eaten

    # Calculate the total calorie deficit needed to lose 10 pounds
    total_calorie_deficit = pounds_to_lose * calories_needed_to_lose_1lb

    # Calculate the number of days needed to reach the total calorie deficit
    num_days = total_calorie_deficit / daily_calorie_deficit
    result = num_days
    return result

print(solution())