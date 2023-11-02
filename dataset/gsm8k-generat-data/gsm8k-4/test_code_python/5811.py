def solution():
    """Julie started her own landscaping business. She charges $4 an hour for mowing lawns and $8 for pulling weeds. In September she mowed lawns for 25 hours and pulled weeds for 3 hours. If she worked the same number of hours in October, how much money did she earn in September and October?"""
    # Define the prices per hour and the number of hours worked
    lawn_price = 4
    weed_price = 8
    september_lawn_hours = 25
    september_weed_hours = 3
    october_lawn_hours = 25
    october_weed_hours = 3

    # Calculate the earnings for September and October
    september_earnings = (september_lawn_hours * lawn_price) + (september_weed_hours * weed_price)
    october_earnings = (october_lawn_hours * lawn_price) + (october_weed_hours * weed_price)

    # Calculate the total earnings
    total_earnings = september_earnings + october_earnings

    # return the result
    result = total_earnings
    return result

print(solution())