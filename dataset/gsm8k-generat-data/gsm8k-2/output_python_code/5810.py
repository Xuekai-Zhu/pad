def solution():
    """Julie started her own landscaping business. She charges $4 an hour for mowing lawns and $8 for pulling weeds. In September she mowed lawns for 25 hours and pulled weeds for 3 hours. If she worked the same number of hours in October, how much money did she earn in September and October?"""
    lawn_rate = 4
    weed_rate = 8
    sep_lawn_hours = 25
    sep_weed_hours = 3
    sep_earnings = (sep_lawn_hours * lawn_rate) + (sep_weed_hours * weed_rate)
    oct_hours = sep_lawn_hours + sep_weed_hours
    oct_earnings = oct_hours * (lawn_rate + weed_rate)
    total_earnings = sep_earnings + oct_earnings
    result = total_earnings
    return result

print(solution())