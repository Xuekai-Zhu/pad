def solution():
    """On a farm, on average every 6 cows produce 108 liters of milk per week. In five weeks the cows produced 2160 liters of milk. How many cows are on the farm?"""
    liters_per_week = 108
    weeks = 5
    total_liters = 2160
    liters_per_cow_per_week = liters_per_week / 6
    total_cows = total_liters / (liters_per_cow_per_week * weeks)
    result = total_cows
    return result

print(solution())