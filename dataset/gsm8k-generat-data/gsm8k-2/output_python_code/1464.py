def solution():
    """Jack goes up three flights of stairs, then down six flights of stairs. If each flight of stairs has 12 steps that each each 8 inches high, how many feet further down is Jack than when he started?"""
    up_flights = 3
    down_flights = 6
    steps_per_flight = 12
    step_height_inches = 8
    total_distance_up = up_flights * steps_per_flight * step_height_inches
    total_distance_down = down_flights * steps_per_flight * step_height_inches
    net_distance = total_distance_up - total_distance_down
    distance_feet = net_distance / 12
    result = distance_feet
    return result

print(solution())