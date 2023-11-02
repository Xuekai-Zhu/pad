def solution():
    """Grace started her own landscaping business. She charges $6 an hour for mowing lawns, $11 for pulling weeds and $9 for putting down mulch. In September she mowed lawns for 63 hours, pulled weeds for 9 hours and put down mulch for 10 hours. How much money did she earn in September?"""
    # Define the hourly rates for each service
    mow_rate = 6
    weed_rate = 11
    mulch_rate = 9

    # Calculate the total earnings for mowing lawns
    mow_earnings = mow_rate * 63

    # Calculate the total earnings for pulling weeds
    weed_earnings = weed_rate * 9

    # Calculate the total earnings for putting down mulch
    mulch_earnings = mulch_rate * 10

    # Calculate the overall earnings for September
    total_earnings = mow_earnings + weed_earnings + mulch_earnings

    result = total_earnings
    return result

print(solution())