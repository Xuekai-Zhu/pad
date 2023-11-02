def solution():
    blue_speed = 80  # Blue car can travel at a speed of 80 miles per hour
    green_speed = blue_speed * 8  # Green car can travel at 8 times the speed of blue car
    red_speed = green_speed * 2  # Red car can travel at twice the speed of green car
    # Yellow car is broken and cannot move

    result = red_speed
    return result

print(solution())