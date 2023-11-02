def solution():
    """Ms. Warren ran at 6 mph for 20 minutes. After the run, she walked at 2 mph for 30 minutes. How many miles did she run and walk in total?"""
    run_speed = 6 / 60  # convert to miles/min
    run_time = 20
    run_distance = run_speed * run_time
    walk_speed = 2 / 60  # convert to miles/min
    walk_time = 30
    walk_distance = walk_speed * walk_time
    total_distance = run_distance + walk_distance
    result = total_distance
    return result

print(solution())