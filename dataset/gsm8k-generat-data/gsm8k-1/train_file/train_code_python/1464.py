def solution():
    """Jack goes up three flights of stairs, then down six flights of stairs. If each flight of stairs has 12 steps that each each 8 inches high, how many feet further down is Jack than when he started?"""
    up_flights = 3
    down_flights = 6
    steps_per_flight = 12
    step_height = 8/12  # converting inches to feet
    total_steps = up_flights * steps_per_flight - down_flights * steps_per_flight
    distance_travelled = total_steps * step_height
    result = distance_travelled
    return result

print(solution())