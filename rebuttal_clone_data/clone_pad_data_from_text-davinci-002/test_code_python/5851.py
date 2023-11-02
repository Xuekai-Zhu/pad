def solution():
    temp_avg = 90
    cricket_eating_rate = 4
    temp_avg_2 = 100
    cricket_eating_rate_2 = cricket_eating_rate * 2
    num_weeks = 15
    time_90 = 0.8
    time_100 = 0.2
    cricket_eating_rate_overall = (time_90 * cricket_eating_rate) + (time_100 * cricket_eating_rate_2)
    total_crickets = cricket_eating_rate_overall * num_weeks
    result = total_crickets
    return result

print(solution())