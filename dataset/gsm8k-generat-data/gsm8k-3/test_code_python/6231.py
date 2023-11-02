def solution():
    """Ms. Warren ran at 6 mph for 20 minutes. After the run, she walked at 2 mph for 30 minutes. How many miles did she run and walk in total?"""
    # Convert minutes to hours
    run_time = 20/60
    walk_time = 30/60

    # Calculate the distance run
    run_distance = 6 * run_time

    # Calculate the distance walked
    walk_distance = 2 * walk_time

    # Calculate the total distance
    total_distance = run_distance + walk_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())