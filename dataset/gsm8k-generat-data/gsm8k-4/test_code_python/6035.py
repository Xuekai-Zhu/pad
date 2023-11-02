def solution():
    """Cherry put up a delivery service. She charges $2.50 for a 3-5 kilograms cargo and $4 for a 6-8 kilograms cargo. If she delivers four 5 kilograms cargo and two 8 kilograms cargo per day, how much money will she earn in a week?"""
    # Define the prices and weight limits
    PRICE_SMALL = 2.5
    PRICE_LARGE = 4.0
    SMALL_WEIGHT_LIMIT = 5
    LARGE_WEIGHT_LIMIT = 8

    # Calculate the earnings for each cargo delivered
    small_earnings = PRICE_SMALL
    large_earnings = PRICE_LARGE

    # Calculate the total earnings for each day
    day_earnings = (small_earnings * 4 * 5) + (large_earnings * 2 * 8)

    # Calculate the total earnings for the week
    week_earnings = day_earnings * 7

    result = week_earnings
    return result

print(solution())