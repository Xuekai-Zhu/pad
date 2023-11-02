def solution():
    """Julie started her own landscaping business. She charges $4 an hour for mowing lawns and $8 for pulling weeds. In September she mowed lawns for 25 hours and pulled weeds for 3 hours. If she worked the same number of hours in October, how much money did she earn in September and October?"""
    # Define the rates for mowing lawns and pulling weeds
    LAWN_RATE = 4
    WEED_RATE = 8

    # Define the number of hours worked in September
    sep_hours = 25

    # Calculate the amount earned in September
    sep_earnings = (sep_hours * LAWN_RATE) + (3 * WEED_RATE)

    # Calculate the amount earned in October (assuming same hours worked)
    oct_earnings = (sep_earnings / sep_hours) * sep_hours

    # Calculate the total earnings for September and October
    total_earnings = sep_earnings + oct_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())