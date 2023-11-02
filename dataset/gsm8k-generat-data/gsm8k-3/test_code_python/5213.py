def solution():
    """ Jon decides to take up baseball. He can throw a fastball at 80 miles per hour. He goes through intense training 4 times for 4 weeks each time and at the end of the last one he can throw a ball 20% faster. How much speed (in mph) did he gain per week, assuming he gained an equal amount of speed (in mph) each week? """

    # Jon's initial fastball speed
    initial_speed = 80

    # Jon's final fastball speed after training
    final_speed = initial_speed * 1.2

    # Number of weeks Jon spent training
    weeks = 4 * 4

    # Average increase in speed per week
    speed_increase_per_week = (final_speed - initial_speed) / weeks

    result = speed_increase_per_week
    return result

print(solution())