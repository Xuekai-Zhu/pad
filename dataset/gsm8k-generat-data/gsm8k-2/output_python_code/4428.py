def solution():
    """Ivy drinks 2.5 liters of water each day. How many bottles of 2-liter water should Ivy buy for her 4 days consumption?"""
    water_per_day = 2.5
    days = 4
    total_water = water_per_day * days
    bottles_needed = total_water / 2
    result = bottles_needed
    return result

print(solution())