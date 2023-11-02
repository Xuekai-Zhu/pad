def solution():
    """Dale owns 4 sports cars. The red one can travel at twice the speed of the green one, but the green one can travel at 8 times the speed of the blue one. The yellow one is broken and cannot move at all. If the blue one can travel at a speed of 80 miles per hour, at what speed, in miles per hour, can the red car travel?"""
    # Define the speed of the blue car
    blue_speed = 80

    # Calculate the speed of the green car
    green_speed = blue_speed * 8

    #Calculate the speed of the red car
    red_speed = green_speed * 2

    # Return the speed of the red car
    result = red_speed
    return result

print(solution())