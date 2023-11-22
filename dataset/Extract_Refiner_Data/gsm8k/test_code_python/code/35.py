def solution():
    
    # Define Dana's speeds
    RUN_SPEED = 3
    WALK_SPEED = RUN_SPEED * 4
    SKIP_SPEED = RUN_SPEED / 2

    # Define the time spent running and walking
    running_time = 6 / 3
    walking_time = 6 / 2

    # Calculate Dana's speeds
    run_speed = RUN_SPEED / (1/3)
    walk_speed = WALK_SPEED / (2/3)
    skip_speed = SKIP_SPEED / (1/2)

    # Calculate Dana's total distance
    total_distance = run_speed * running_time + walk_speed * walking_time + skip_speed * 6

    # Display Dana's total distance
    result = total_distance
    return result

print(solution())