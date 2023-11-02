def solution():
    swim_distance = 2 * 2  # Tom swims for 2 hours at a speed of 2 miles per hour
    run_time = 2 / 2  # Tom runs for half the time he swam
    run_speed = 2 * 4  # Tom runs 4 times as fast as he swims
    run_distance = run_time * run_speed  # distance covered while running
    total_distance = swim_distance + run_distance  # total distance covered
    result = total_distance
    return result

print(solution())