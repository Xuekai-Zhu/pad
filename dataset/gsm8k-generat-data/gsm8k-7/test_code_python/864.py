def solution():
    cups_weekday_per_day = 10
    cups_weekday_per_week = 5 * cups_weekday_per_day  # 50 cups per week on weekdays

    cups_weekend = 120
    cups_weekday = (7 * cups_weekday_per_day) - cups_weekend  # 10 cups per hour x 5 hours x 7 days = 350, so 350 - 120 = 230 cups on weekdays

    total_cups_per_week = cups_weekday + cups_weekend
    result = total_cups_per_week
    return result

print(solution())