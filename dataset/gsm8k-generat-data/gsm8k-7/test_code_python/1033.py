def solution():
    calories_lost_per_hour_dancing = 2 * 300  # James burns twice as many calories as when walking
    num_dances_per_day = 2
    duration_per_dance = 0.5
    num_days_per_week = 4

    # Calculate the total time spent dancing each week
    total_time_dancing = num_dances_per_day * duration_per_dance * num_days_per_week

    # Calculate the total calories lost from dancing each week
    total_calories_lost = calories_lost_per_hour_dancing * total_time_dancing

    result = total_calories_lost
    return result

print(solution())