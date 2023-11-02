def solution():
    base_speed = 80
    percent_increase = 20
    speed_increase = base_speed * (percent_increase / 100)
    total_weeks = 4
    weeks_per_training = 4
    total_weeks_trained = total_weeks * weeks_per_training
    speed_per_week = speed_increase / total_weeks_trained
    result = speed_per_week
    return result

print(solution())