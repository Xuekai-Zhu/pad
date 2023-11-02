def solution():
    """Jenna works as a truck driver. She gets paid $0.40 cents per mile. If she drives 400 miles one way, how much does she get paid for a round trip?"""
    miles_per_trip = 400 * 2
    pay_per_mile = 0.40
    total_pay = miles_per_trip * pay_per_mile
    result = total_pay
    return result

print(solution())