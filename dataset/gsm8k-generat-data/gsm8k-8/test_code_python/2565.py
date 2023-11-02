def solution():
    # Define the distance of each flight in feet
    flight_distance = 10

    # Convert each step distance from inches to feet
    step_distance = 18 / 12

    # Calculate the number of steps John climbs
    num_steps = 9 * flight_distance / step_distance

    result = num_steps
    return result

print(solution())