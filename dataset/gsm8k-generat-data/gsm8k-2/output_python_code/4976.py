def solution():
    """A desert garden’s sprinkler system runs twice a day during the cool morning and evening hours. It waters the garden with four liters of water in the morning and six liters in the evening. How many days does it take the sprinkler system to use 50 liters of water?"""
    morning_water = 4
    evening_water = 6
    total_water_per_day = morning_water + evening_water
    total_water_needed = 50
    days_to_reach_total = total_water_needed / total_water_per_day
    result = days_to_reach_total
    return result

print(solution())