def solution():
    """ Jenna works as a truck driver. She gets paid $0.40 cents per mile. If she drives 400 miles one way, how much does she get paid for a round trip?"""
    # Define the rate per mile and the distance traveled one way
    rate_per_mile = 0.40
    distance_one_way = 400

    # Calculate the total distance traveled for a round trip
    distance_round_trip = distance_one_way * 2

    # Calculate the total pay for a round trip
    pay_round_trip = distance_round_trip * rate_per_mile

    result = pay_round_trip
    return result

print(solution())