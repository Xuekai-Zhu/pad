def solution():
    """Every day Tom drinks 5 12-oz cans of soda plus 64 ounces of water. How many ounces of fluid does he drink a week?"""
    soda_oz = 12
    water_oz = 64
    total_fluid_oz = (soda_oz * 5) + water_oz
    fluid_per_week = total_fluid_oz * 7
    result = fluid_per_week
    return result

print(solution())