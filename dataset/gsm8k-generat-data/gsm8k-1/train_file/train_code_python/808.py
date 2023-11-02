def solution():
    """If Clover goes for a 1.5-mile walk in the morning and another 1.5-mile walk in the evening, every day, how many miles does he walk in 30 days?"""
    miles_per_walk = 1.5
    walks_per_day = 2
    days = 30
    total_miles = miles_per_walk * walks_per_day * days
    result = total_miles
    return result

print(solution())