def solution():
    # Total minutes in 5 hours
    total_minutes = 5 * 60

    # Time per battery
    time_per_battery = 6 + 9

    # Batteries per robot per minute
    batteries_per_robot_per_minute = 60 / time_per_battery

    # Total batteries per minute for all robots
    total_batteries_per_minute = 10 * batteries_per_robot_per_minute

    # Total batteries in 5 hours
    total_batteries = total_batteries_per_minute * total_minutes

    result = total_batteries
    return result

print(solution())