def solution():
    """Ms. Warren ran at 6 mph for 20 minutes. After the run, she walked at 2 mph for 30 minutes. How many miles did she run and walk in total?"""
    # Define the speed and time of the run
    run_speed = 6
    run_time = 20/60

    # Calculate the distance of the run
    run_distance = run_speed * run_time

    # Define the speed and time of the walk
    walk_speed = 2
    walk_time = 30/60

    # Calculate the distance of the walk
    walk_distance = walk_speed * walk_time

    # Calculate the total distance
    total_distance = run_distance + walk_distance

    # Return the result
    result = total_distance
    return result

print(solution())