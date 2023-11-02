def solution():
    daily_calories = 2500
    saturday_calories = 1000
    daily_burn = 3000

    # Calculate the calories consumed from Sunday to Friday
    weekday_calories = daily_calories * 6

    # Calculate the calories consumed on Saturday
    saturday_total_calories = daily_calories + saturday_calories

    # Calculate the total calories consumed in the week
    total_calories = weekday_calories + saturday_total_calories

    # Calculate the total calories burned in the week
    total_burned = daily_burn * 7

    # Calculate the weekly caloric deficit
    weekly_deficit = total_burned - total_calories
    result = weekly_deficit
    return result

print(solution())