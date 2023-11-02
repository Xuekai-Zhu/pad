def solution():
    """Jenna works as a truck driver. She gets paid $0.40 cents per mile. If she drives 400 miles one way, how much does she get paid for a round trip?"""
    distance_one_way = 400
    distance_round_trip = distance_one_way * 2
    payment_per_mile = 0.40
    total_payment = distance_round_trip * payment_per_mile
    result = total_payment
    return result

print(solution())