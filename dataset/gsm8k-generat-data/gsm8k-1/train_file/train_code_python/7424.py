def solution():
    """Lars owns a bakeshop. She can bake 10 loaves of bread within an hour and 30 baguettes every 2 hours. If she bakes 6 hours a day, how many breads does she makes?"""
    breads_per_hour = 10
    baguettes_per_two_hours = 30
    total_breads = (breads_per_hour * 6) + (baguettes_per_two_hours * 3)
    result = total_breads
    return result

print(solution())