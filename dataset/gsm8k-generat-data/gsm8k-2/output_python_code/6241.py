def solution():
    """Tim drinks 2 bottles that are each 1.5 quarts and an additional 20 ounces a day. How much water does he drink a week?"""
    bottles_per_day = 2
    bottle_size = 1.5 # in quarts
    additional_water = 20 / 32 # converting 20 ounces to quarts
    total_water_per_day = (bottles_per_day * bottle_size) + additional_water
    total_water_per_week = total_water_per_day * 7
    result = total_water_per_week
    return result

print(solution())