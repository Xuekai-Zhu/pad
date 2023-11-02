def solution():
    """Dale owns 4 sports cars. The red one can travel at twice the speed of the green one, but the green one can travel at 8 times the speed of the blue one.  The yellow one is broken and cannot move at all.  If the blue one can travel at a speed of 80 miles per hour, at what speed, in miles per hour, can the red car travel?"""
    # Define the speed of the blue car
    BLUE_SPEED = 80

    # Calculate the speed of the green car
    GREEN_SPEED = BLUE_SPEED * 8

    # Calculate the speed of the red car
    RED_SPEED = GREEN_SPEED * 2

    # Display the speed of the red car
    result = RED_SPEED
    return result

print(solution())