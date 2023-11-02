def solution():
    # Define the boat trip duration
    boat_trip = 2

    # Calculate the plane trip duration
    plane_trip = 4 * boat_trip

    # Calculate the total trip duration
    total_trip = plane_trip + boat_trip

    result = total_trip
    return result

print(solution())