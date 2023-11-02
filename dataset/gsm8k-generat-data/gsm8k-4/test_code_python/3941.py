def solution():
    """Timmy plans to ride a skateboard ramp that is 50 feet high. He knows he needs to go 40 mph at the start to make it all the way to the top. He measures his speed on three trial runs and goes 36, 34, and 38 mph. How much faster does he have to go than his average speed to make it up the ramp?"""
    # Define the height of the ramp and the target speed
    ramp_height = 50
    target_speed = 40

    # Calculate Timmy's average speed on the three trial runs
    average_speed = (36 + 34 + 38) / 3

    # Calculate the speed difference needed to reach the top of the ramp
    speed_difference = target_speed - average_speed

    result = speed_difference
    return result

print(solution())