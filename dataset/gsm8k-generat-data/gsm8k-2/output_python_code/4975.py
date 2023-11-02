def solution():
    """There are 10 6-ounces of glasses that are only 4/5 full of water. How many ounces of water are needed to fill to the brim all those 10 glasses?"""
    glasses_full = 10
    glass_size = 6
    fullness_ratio = 4/5
    total_water_needed = glasses_full * glass_size * (1-fullness_ratio)
    result = total_water_needed
    return result

print(solution())