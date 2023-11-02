def solution():
    """Jenna works as a truck driver. She gets paid $0.40 cents per mile. If she drives 400 miles one way, how much does she get paid for a round trip?"""
    # Define the rate per mile
    RATE_PER_MILE = 0.40

    # Calculate the pay for the round trip
    round_trip_pay = 2 * RATE_PER_MILE * 400

    # Display the pay for the round trip
    result = round_trip_pay
    return result

print(solution())