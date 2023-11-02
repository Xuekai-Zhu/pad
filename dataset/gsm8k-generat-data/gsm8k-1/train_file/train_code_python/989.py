def solution():
    """Grace started her own landscaping business. She charges $6 an hour for mowing lawns, $11 for pulling weeds and $9 for putting down mulch. In September she mowed lawns for 63 hours, pulled weeds for 9 hours and put down mulch for 10 hours. How much money did she earn in September?"""
    lawn_hourly_rate = 6
    weed_hourly_rate = 11
    mulch_hourly_rate = 9
    lawn_hours = 63
    weed_hours = 9
    mulch_hours = 10
    
    lawn_money = lawn_hours * lawn_hourly_rate
    weed_money = weed_hours * weed_hourly_rate
    mulch_money = mulch_hours * mulch_hourly_rate
    
    total_money = lawn_money + weed_money + mulch_money
    result = total_money
    
    return result

print(solution())