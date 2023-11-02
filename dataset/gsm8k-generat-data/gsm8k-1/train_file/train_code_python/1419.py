def solution():
    """Compared to the amount of water she drank, Carla drank three times as much soda minus 6 ounces. If she drank 54 ounces of liquid total, how much water did she drink?"""
    total_drinks = 54
    soda_ratio = 3
    soda_ounces = ((soda_ratio * water_ounces) - 6)
    water_ounces = (total_drinks - soda_ounces)
    result = water_ounces
    return result

print(solution())