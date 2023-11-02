def solution():
    # Calculate the number of Dutch people on the bus
    dutch_on_bus = 90 * (3/5)

    # Calculate the number of Dutch Americans on the bus
    dutch_americans = dutch_on_bus * (1/2)

    # Calculate the number of Dutch Americans who got window seats
    windows_seats = dutch_americans * (1/3)
    result = windows_seats
    return result

print(solution())