def solution():
    """Ben works 8-hour shifts in a furniture shop. It takes him 5 hours to build 1 rocking chair. How many chairs can he build in 10 days?"""
    hours_per_shift = 8
    hours_per_chair = 5
    chairs_per_day = hours_per_shift // hours_per_chair
    days = 10
    total_chairs = chairs_per_day * days
    result = total_chairs
    return result

print(solution())