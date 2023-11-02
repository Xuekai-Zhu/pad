def solution():
    """John climbs up 9 flights of stairs. Each flight is 10 feet. If each step is 18 inches, how many steps does he climb up?"""
    flight_distance = 10 * 12  # feet to inches
    step_length = 18  # inches
    steps_per_flight = flight_distance / step_length
    total_steps = steps_per_flight * 9
    result = total_steps
    return result

print(solution())