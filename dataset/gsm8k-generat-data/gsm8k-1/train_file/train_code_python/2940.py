def solution():
    """Francine drives 140km to work each day. If she does not go to work 3 days every week, find the total distance she drives to work for 4 weeks in kilometers."""
    distance_per_day = 140
    days_per_week = 5
    weeks = 4
    days_skip = 3
    total_days_worked = (days_per_week * weeks) - days_skip
    total_distance = total_days_worked * distance_per_day
    result = total_distance
    return result

print(solution())