def solution():
    milo_run_speed = x  # Milo's running speed in miles per hour
    milo_skate_speed = 2 * milo_run_speed  # Milo's skateboarding speed is twice his running speed
    cory_wheelchair_speed = 12  # Cory's wheelchair speed is 12 miles per hour

    # Calculate the distance Milo can travel in two hours
    distance_milo_in_two_hours = milo_run_speed * 2 + milo_skate_speed * 2 + cory_wheelchair_speed * 2

    # Calculate the distance Milo can run in two hours
    distance_milo_run_in_two_hours = distance_milo_in_two_hours - (milo_skate_speed * 2)

    result = distance_milo_run_in_two_hours
    return result

print(solution())