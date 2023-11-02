def solution():
    """Francine drives 140km to work each day. If she does not go to work 3 days every week, find the total distance she drives to work for 4 weeks in kilometers."""
    daily_distance = 140
    days_per_week = 7
    work_days_per_week = days_per_week - 3
    total_distance_per_week = daily_distance * work_days_per_week
    total_distance_per_four_weeks = total_distance_per_week * 4
    result = total_distance_per_four_weeks
    return result

print(solution())