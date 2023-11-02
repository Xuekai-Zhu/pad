def solution():
    """Timmy plans to ride a skateboard ramp that is 50 feet high. He knows he needs to go 40 mph at the start to make it all the way to the top. He measures his speed on three trial runs and goes 36, 34, and 38 mph. How much faster does he have to go than his average speed to make it up the ramp?"""
    # Define the required speed to make it up the ramp
    REQUIRED_SPEED = 40

    # Define the height of the ramp
    RAMP_HEIGHT = 50

    # Define Timmy's measured speeds
    speeds = [36, 34, 38]

    # Calculate Timmy's average speed
    average_speed = sum(speeds) / len(speeds)

    # Calculate how much faster Timmy needs to go than his average speed to make it up the ramp
    speed_difference = REQUIRED_SPEED - average_speed

    # Display how much faster Timmy needs to go
    result = speed_difference
    return result

print(solution())