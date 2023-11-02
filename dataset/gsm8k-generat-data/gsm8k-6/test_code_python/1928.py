def solution():
    # Calculate the total number of passengers transported in one round trip
    round_trip_passengers = 100 + 60  # passengers carried from one station to the other and back again
    # Calculate the total number of passengers transported in four round trips
    total_passengers = 4 * round_trip_passengers  # three more round trips in addition to the first one
    result = total_passengers
    return result

print(solution())