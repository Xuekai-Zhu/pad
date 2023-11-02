def solution():
    """Jon decides to take up baseball. He can throw a fastball at 80 miles per hour. He goes through intense training 4 times for 4 weeks each time and at the end of the last one he can throw a ball 20% faster. How much speed (in mph) did he gain per week, assuming he gained an equal amount of speed (in mph) each week?"""
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