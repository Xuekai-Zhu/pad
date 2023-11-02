def solution():
    """John climbs up 9 flights of stairs. Each flight is 10 feet. If each step is 18 inches, how many steps does he climb up?"""
    flights = 9
    height_per_flight = 10 * 12  # in inches
    step_height = 18
    total_steps = (flights * height_per_flight) // step_height
    result = total_steps
    return result

print(solution())