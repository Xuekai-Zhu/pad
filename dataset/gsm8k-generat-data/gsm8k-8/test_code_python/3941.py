def solution():
    # Define Timmy's target speed
    target_speed = 40

    # Calculate Timmy's average speed
    trial1_speed = 36
    trial2_speed = 34
    trial3_speed = 38
    average_speed = (trial1_speed + trial2_speed + trial3_speed) / 3

    # Calculate how much faster Timmy needs to go than his average speed
    speed_difference = target_speed - average_speed
    result = speed_difference
    return result

print(solution())