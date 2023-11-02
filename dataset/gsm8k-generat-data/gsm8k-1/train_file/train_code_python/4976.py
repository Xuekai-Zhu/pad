def solution():
    """A desert garden’s sprinkler system runs twice a day during the cool morning and evening hours. It waters the garden with four liters of water in the morning and six liters in the evening. How many days does it take the sprinkler system to use 50 liters of water?"""
    morning_liters = 4
    evening_liters = 6
    total_liters_per_day = morning_liters + evening_liters
    days_to_reach_50_liters = 50 / total_liters_per_day
    result = days_to_reach_50_liters
    return result

print(solution())