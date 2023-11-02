def solution():
    time_to_gather = 6
    time_to_create = 9
    robots = 10
    minutes_in_hour = 60
    hours = 5
    total_time = time_to_gather + time_to_create
    robot_hours = robots * hours
    total_batteries = robot_hours * minutes_in_hour / total_time
    result = total_batteries
    return result

print(solution())