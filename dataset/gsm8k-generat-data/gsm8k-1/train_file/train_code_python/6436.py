def solution():
    """A factory uses robots to manufacture batteries. For each battery that is made, it takes a robot 6 minutes to gather the materials for the battery and 9 minutes to create the battery. If the factory has 10 robots working on batteries at the same time, how many batteries can the robots manufacture in 5 hours?"""
    minutes_per_battery = 6 + 9
    batteries_per_minute = 60 / minutes_per_battery  # batteries made per minute per robot
    batteries_per_hour_per_robot = batteries_per_minute * 60  # batteries made per robot per hour
    total_robots = 10
    batteries_per_hour = batteries_per_hour_per_robot * total_robots  # batteries made per hour for all robots
    batteries_per_5_hours = batteries_per_hour * 5  # batteries made in 5 hours
    result = batteries_per_5_hours
    return result

print(solution())