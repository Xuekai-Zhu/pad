def solution():
    """Ms. Warren ran at 6 mph for 20 minutes. After the run, she walked at 2 mph for 30 minutes. How many miles did she run and walk in total?"""
    run_speed = 6/60  # mph to m/min
    walk_speed = 2/60  # mph to m/min
    run_time = 20  # minutes
    walk_time = 30  # minutes
    run_distance = run_speed * run_time  # miles
    walk_distance = walk_speed * walk_time  # miles
    total_distance = run_distance + walk_distance  # miles
    result = total_distance
    return result

print(solution())