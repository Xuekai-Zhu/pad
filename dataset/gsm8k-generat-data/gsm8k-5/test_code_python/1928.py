def solution():
    # Calculate the total number of passengers transported in the first trip
    passengers_first_trip = 100

    # Calculate the total number of passengers transported in the return trip
    passengers_return_trip = 60

    # Calculate the total number of passengers transported in three more round trips
    passengers_more_round_trips = 3 * passengers_first_trip

    # Calculate the total number of passengers transported in both directions
    total_passengers = (passengers_first_trip + passengers_return_trip) * 2 + passengers_more_round_trips

    result = total_passengers
    return result

print(solution())