def solution():
    weekday_cups = 10 * 5 * 5  # 10 cups per hour, 5 hours per day, 5 weekdays in a week
    weekend_cups = 120  # 120 cups brewed on the weekend
    total_cups = weekday_cups + weekend_cups  # Total cups brewed in 1 week
    result = total_cups
    return result

print(solution())