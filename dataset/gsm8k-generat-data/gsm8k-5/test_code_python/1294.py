def solution():
    boat_trip = 2  # The boat trip takes 2 hours
    plane_trip = 4 * boat_trip  # The plane trip is four times longer than the boat trip
    total_trip = boat_trip + plane_trip  # Tom needs to take both the plane and the boat trip

    # Calculate the total time it takes Tom to get to the island
    total_time = boat_trip + plane_trip
    result = total_time
    return result

print(solution())