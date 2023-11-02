def solution():
    # Calculate the total number of passengers on the first trip
    first_trip = 100

    # Calculate the total number of passengers on the return trip
    return_trip = 60

    # Calculate the total number of round trips made
    total_round_trips = 3

    # Calculate the total number of passengers transported in all the trips
    total_passengers = (first_trip + return_trip) * 2 + first_trip * total_round_trips

    result = total_passengers
    return result

print(solution())