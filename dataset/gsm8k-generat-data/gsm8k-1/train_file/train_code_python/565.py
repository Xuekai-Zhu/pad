def solution():
    """Dale owns 4 sports cars. The red one can travel at twice the speed of the green one, but the green one can travel at 8 times the speed of the blue one. The yellow one is broken and cannot move at all. If the blue one can travel at a speed of 80 miles per hour, at what speed, in miles per hour, can the red car travel?"""
    blue_speed = 80
    green_speed = blue_speed * 8
    red_speed = green_speed * 2
    result = red_speed
    return result

print(solution())