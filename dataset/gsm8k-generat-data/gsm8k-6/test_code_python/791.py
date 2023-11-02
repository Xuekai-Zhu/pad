def solution():
    # Calculate the number of Dutch people on the bus
    dutch_people = (3/5) * 90

    # Calculate the number of Dutch Americans on the bus
    dutch_americans = (1/2) * dutch_people

    # Calculate the number of Dutch Americans who got window seats
    window_seats = (1/3) * dutch_americans

    result = window_seats
    return result

print(solution())