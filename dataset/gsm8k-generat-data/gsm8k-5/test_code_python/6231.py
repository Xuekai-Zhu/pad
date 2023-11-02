def solution():
    run_speed = 6 / 60  # Convert mph to miles per minute
    run_time = 20  # Ms. Warren ran for 20 minutes
    run_distance = run_speed * run_time  # Calculate the distance she ran

    walk_speed = 2 / 60  # Convert mph to miles per minute
    walk_time = 30  # Ms. Warren walked for 30 minutes
    walk_distance = walk_speed * walk_time  # Calculate the distance she walked

    # Calculate the total distance she covered
    total_distance = run_distance + walk_distance
    result = total_distance
    return result

print(solution())