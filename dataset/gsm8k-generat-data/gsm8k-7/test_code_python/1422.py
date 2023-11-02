def solution():
    num_collisions_per_minute = 6  # 60 seconds / 10 seconds/collision
    num_big_crashes_per_minute = 3  # 60 seconds / 20 seconds/crash
    num_minutes = 4

    # Calculate the total number of collisions in 4 minutes
    total_collisions = num_collisions_per_minute * num_minutes

    # Calculate the total number of big crashes in 4 minutes
    total_big_crashes = num_big_crashes_per_minute * num_minutes

    # Calculate the overall number of accidents in 4 minutes
    overall_accidents = total_collisions + total_big_crashes
    result = overall_accidents
    return result

print(solution())