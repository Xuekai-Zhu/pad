def solution():
    daily_calories = 2500  # Jonathan consumes 2500 calories every day except Saturday
    saturday_calories = 3500  # Jonathan consumes 3500 calories on Saturday
    daily_burned_calories = 3000  # Jonathan burns 3000 calories every day

    # Calculate the total calories consumed and burned for the week
    total_consumed = (daily_calories * 6) + saturday_calories  # 6 days at 2500 calories and 1 day at 3500 calories
    total_burned = daily_burned_calories * 7  # Jonathan burns 3000 calories every day for 7 days

    # Calculate the weekly caloric deficit
    weekly_deficit = total_burned - total_consumed
    result = weekly_deficit
    return result

print(solution())