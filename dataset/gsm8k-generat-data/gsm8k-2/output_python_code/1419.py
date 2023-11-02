def solution():
    """Compared to the amount of water she drank, Carla drank three times as much soda minus 6 ounces. If she drank 54 ounces of liquid total, how much water did she drink?"""
    total_drink = 54
    soda = (3 * water) - 6
    water = (total_drink - soda) / 4
    result = water
    return result

print(solution())