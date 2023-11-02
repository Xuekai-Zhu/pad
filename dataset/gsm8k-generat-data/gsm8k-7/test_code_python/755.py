def solution():
    swim_time = 2
    swim_speed = 2
    run_time = swim_time / 2
    run_speed = 2 * swim_speed

    # Calculate the distance swam
    swim_distance = swim_time * swim_speed

    # Calculate the distance ran
    run_distance = run_time * run_speed

    # Calculate the total distance covered
    total_distance = swim_distance + run_distance
    result = total_distance
    return result

print(solution())