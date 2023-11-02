def solution():
    # Define the distance of one way trip
    distance = 400

    # Calculate the earnings for one way trip
    earnings_one_way = distance * 0.40

    # Calculate the earnings for round trip
    earnings_round_trip = earnings_one_way * 2
    result = earnings_round_trip
    return result

print(solution())