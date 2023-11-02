def solution():
    """John climbs up 9 flights of stairs. Each flight is 10 feet. If each step is 18 inches, how many steps does he climb up?"""
    # Define the number of flights and the height of each flight
    flights = 9
    flight_height = 10 * 12

    # Calculate the total height John climbs up
    total_height = flights * flight_height

    # Calculate the number of steps John takes
    step_length = 18 / 12
    total_steps = total_height / step_length

    # Round the result to the nearest whole number
    result = round(total_steps)
    return result

print(solution())