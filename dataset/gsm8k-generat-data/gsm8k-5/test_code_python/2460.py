def solution():
    payment_per_mile = 0.40  # Jenna gets paid $0.40 per mile
    distance_one_way = 400  # Jenna drives 400 miles one way

    # Calculate the payment for the round trip
    payment_round_trip = 2 * distance_one_way * payment_per_mile

    result = payment_round_trip
    return result

print(solution())