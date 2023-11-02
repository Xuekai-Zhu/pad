def solution():
    """Grace started her own landscaping business. She charges $6 an hour for mowing lawns, $11 for pulling weeds and $9 for putting down mulch. In September she mowed lawns for 63 hours, pulled weeds for 9 hours and put down mulch for 10 hours. How much money did she earn in September?"""
    # Define the hourly rates for each service
    LAWN_RATE = 6
    WEED_RATE = 11
    MULCH_RATE = 9

    # Define the number of hours worked for each service
    lawn_hours = 63
    weed_hours = 9
    mulch_hours = 10

    # Calculate the earnings for each service
    lawn_earnings = lawn_hours * LAWN_RATE
    weed_earnings = weed_hours * WEED_RATE
    mulch_earnings = mulch_hours * MULCH_RATE

    # Calculate the total earnings for September
    total_earnings = lawn_earnings + weed_earnings + mulch_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())