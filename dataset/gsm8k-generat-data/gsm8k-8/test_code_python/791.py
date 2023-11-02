def solution():
    # Calculate the number of Dutch people on the bus
    dutch_people = 0.6 * 90

    # Calculate the number of Dutch Americans on the bus
    dutch_americans = 0.5 * dutch_people

    # Calculate the number of Dutch Americans who got window seats
    dutch_americans_window_seats = (1/3) * dutch_americans
    result = dutch_americans_window_seats
    return result

print(solution())