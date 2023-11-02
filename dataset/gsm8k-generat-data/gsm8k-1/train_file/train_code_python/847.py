def solution():
    """On a farm, on average every 6 cows produce 108 liters of milk per week. In five weeks the cows produced 2160 liters of milk. How many cows are on the farm?"""
    liters_per_week_per_cow = 108
    weeks = 5
    total_liters = 2160
    total_cows = (total_liters / (liters_per_week_per_cow * weeks)) * 6
    result = total_cows
    return result

print(solution())