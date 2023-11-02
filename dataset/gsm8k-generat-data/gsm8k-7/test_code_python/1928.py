def solution():
    passengers_per_trip = 100
    num_round_trips = 3

    # Calculate the total number of passengers transported in one round trip
    total_passengers_per_round_trip = passengers_per_trip + 60

    # Calculate the total number of passengers transported in all round trips
    total_passengers_all_round_trips = total_passengers_per_round_trip * num_round_trips

    # Calculate the total number of passengers transported between both stations
    total_passengers = passengers_per_trip + total_passengers_all_round_trips
    result = total_passengers
    return result

print(solution())