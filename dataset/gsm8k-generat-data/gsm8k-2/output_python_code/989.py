def solution():
    """Grace started her own landscaping business. She charges $6 an hour for mowing lawns, $11 for pulling weeds and $9 for putting down mulch. In September she mowed lawns for 63 hours, pulled weeds for 9 hours and put down mulch for 10 hours. How much money did she earn in September?"""
    lawn_price = 6
    weed_price = 11
    mulch_price = 9
    lawn_hours = 63
    weed_hours = 9
    mulch_hours = 10
    total_money = (lawn_price * lawn_hours) + (weed_price * weed_hours) + (mulch_price * mulch_hours)
    result = total_money
    return result

print(solution())