def solution():
    run_speed = 3
    walk_speed = 1
    time_to_run_one_mile = 1 / run_speed
    time_to_walk_one_mile = 1 / walk_speed
    total_time = time_to_run_one_mile + time_to_walk_one_mile
    result = total_time
    return result

print(solution())