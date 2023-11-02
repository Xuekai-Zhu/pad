def solution():
    num_flights = 9
    flight_height = 10  # in feet
    step_length = 1.5  # in feet (18 inches)

    # Calculate the total height that John climbs up
    total_height = num_flights * flight_height

    # Calculate the total number of steps that John takes
    total_steps = int(total_height / step_length)
    result = total_steps
    return result

print(solution())