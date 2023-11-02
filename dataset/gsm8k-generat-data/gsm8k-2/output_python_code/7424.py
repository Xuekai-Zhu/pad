def solution():
    """Lars owns a bakeshop. She can bake 10 loaves of bread within an hour and 30 baguettes every 2 hours. If she bakes 6 hours a day, how many breads does she makes?"""
    breads_per_hour = 10
    baguettes_every_2_hours = 30
    hours_per_day = 6
    loaves_per_day = breads_per_hour * hours_per_day
    baguettes_per_day = (hours_per_day // 2) * 30
    total_breads_per_day = loaves_per_day + baguettes_per_day
    result = total_breads_per_day
    return result

print(solution())