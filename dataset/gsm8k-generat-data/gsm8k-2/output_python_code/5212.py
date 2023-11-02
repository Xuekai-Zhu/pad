def solution():
    """Jon decides to take up baseball. He can throw a fastball at 80 miles per hour. He goes through intense training 4 times for 4 weeks each time and at the end of the last one he can throw a ball 20% faster. How much speed (in mph) did he gain per week, assuming he gained an equal amount of speed (in mph) each week?"""
    initial_speed = 80
    final_speed = initial_speed * 1.2
    total_weeks = 16
    speed_gain_per_week = (final_speed - initial_speed) / total_weeks
    result = speed_gain_per_week
    return result

print(solution())