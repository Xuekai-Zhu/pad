def solution():
    
    temp_90_avg_weeks = 15 * 0.8
    temp_100_avg_weeks = 15 * 0.2
    crickets_per_week_at_90_degrees = 4
    crickets_per_week_at_100_degrees = 8
    total_crickets = (crickets_per_week_at_90_degrees * temp_90_avg_weeks) + \
                    (crickets_per_week_at_100_degrees * temp_100_avg_weeks)
    result = total_crickets
    return result

print(solution())