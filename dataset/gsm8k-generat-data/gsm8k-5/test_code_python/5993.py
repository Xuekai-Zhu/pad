def solution():
    daily_calorie_deficit = 500  # John needs to burn 500 more calories than he eats to lose 1 pound in a week
    calories_to_lose_1lb = 4000  # It takes burning 4000 calories to lose 1 pound
    days_per_week = 7  # There are 7 days in a week
    pounds_to_lose = 10  # John wants to lose 10 pounds

    # Calculate the number of days it will take John to lose 10 pounds
    total_calories_to_lose = calories_to_lose_1lb * pounds_to_lose
    total_weeks_to_lose = total_calories_to_lose / daily_calorie_deficit / days_per_week
    result = total_weeks_to_lose * days_per_week
    return result

print(solution())