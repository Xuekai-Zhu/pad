def solution():
    # Calculate the speed of the green car
    green_speed = 8 * 80  # the green car can travel at 8 times the speed of the blue one

    # Calculate the speed of the red car
    red_speed = 2 * green_speed  # the red car can travel at twice the speed of the green one

    result = red_speed
    return result

print(solution())