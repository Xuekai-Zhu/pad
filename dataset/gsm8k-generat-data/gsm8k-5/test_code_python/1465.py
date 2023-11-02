def solution():
    # Calculate the vertical distance Jack went up and down
    distance_up = 3 * 12 * 8 / 12  # 3 flights, 12 steps per flight, 8 inches per step, divided by 12 to convert to feet
    distance_down = 6 * 12 * 8 / 12  # 6 flights, 12 steps per flight, 8 inches per step, divided by 12 to convert to feet

    # Calculate the net vertical distance traveled by Jack
    net_distance = distance_down - distance_up
    result = net_distance
    return result

print(solution())