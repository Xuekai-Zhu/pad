def solution():
    
    initial_speed = 80
    training_periods = 4
    weeks_per_period = 4
    percent_speed_increase = 20
    total_weeks = training_periods * weeks_per_period
    speed_increase_per_week = percent_speed_increase / 100 / total_weeks
    speed_increase = initial_speed * percent_speed_increase / 100
    final_speed = initial_speed + speed_increase
    gain_per_week = speed_increase / total_weeks
    result = gain_per_week
    return result

print(solution())