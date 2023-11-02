def solution():
    last_week_hours = 91
    planned_hours = 8 * 7  # 8 hours a day for 7 days

    # Calculate the difference between last week's usage and planned usage for this week
    difference = last_week_hours - planned_hours
    result = difference
    return result

print(solution())