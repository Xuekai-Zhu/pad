def solution():
    # Swimming distance
    swim_distance = 2 * 2  # Distance covered when swimming at 2 miles per hour for 2 hours

    # Running distance
    run_time = 2  # Tom runs for half the time he swam, 1 hour
    run_speed = 4 * 2  # Tom runs 4 times faster than when he was swimming
    run_distance = run_speed * run_time  # Distance covered when running

    # Total distance covered
    total_distance = swim_distance + run_distance
    result = total_distance
    return result

print(solution())