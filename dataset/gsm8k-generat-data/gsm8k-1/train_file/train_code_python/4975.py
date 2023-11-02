def solution():
    """There are 10 6-ounces of glasses that are only 4/5 full of water. How many ounces of water are needed to fill to the brim all those 10 glasses?"""
    glass_capacity = 6
    water_percentage = 4/5
    water_amount = glass_capacity * water_percentage
    empty_space = glass_capacity - water_amount
    total_water_needed = empty_space * 10
    result = total_water_needed
    return result

print(solution())