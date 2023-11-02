def solution():
    # Calculate Milo's speed on his skateboard
    milo_skateboard_speed = 2 * milo_running_speed

    # Calculate Cory's speed
    cory_speed = 12

    # Calculate Milo's running distance in 2 hours
    milo_running_distance = 2 * milo_running_speed * 2

    # Calculate Milo's skateboarding distance in 2 hours
    milo_skateboard_distance = 2 * milo_skateboard_speed * 2

    # Calculate the total distance Milo can travel in 2 hours
    total_distance = milo_running_distance + milo_skateboard_distance

    result = milo_running_distance
    return result

print(solution())