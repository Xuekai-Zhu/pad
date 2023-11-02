def solution():
    # Calculate the total number of passengers
    total_passengers = 50 + 60 + 40

    # Calculate the total passenger miles (passengers * miles flown)
    passenger_miles = (50 * 2) + (60 * 2) + (40 * 2)

    # Calculate the total miles flown by all planes
    total_miles = passenger_miles / 2 + 600 * 3

    # Calculate the average speed
    average_speed = total_miles / 3

    result = average_speed
    return result

print(solution())