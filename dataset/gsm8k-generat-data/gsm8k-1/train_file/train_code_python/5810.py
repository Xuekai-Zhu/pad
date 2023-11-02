def solution():
    """Julie started her own landscaping business. She charges $4 an hour for mowing lawns and $8 for pulling weeds. In September she mowed lawns for 25 hours and pulled weeds for 3 hours. If she worked the same number of hours in October, how much money did she earn in September and October?"""
    mowing_rate = 4
    weeding_rate = 8
    september_mowing_hours = 25
    september_weeding_hours = 3
    october_mowing_hours = 25
    october_weeding_hours = 3

    september_earnings = mowing_rate * september_mowing_hours + weeding_rate * september_weeding_hours
    october_earnings = mowing_rate * october_mowing_hours + weeding_rate * october_weeding_hours

    total_earnings = september_earnings + october_earnings
  
    return total_earnings

print(solution())