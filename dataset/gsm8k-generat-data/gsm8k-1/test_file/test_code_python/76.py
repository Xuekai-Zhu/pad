def solution():
    """Two girls each got 1/6 of the 24 liters of water. Then a boy got 6 liters of water. How many liters of water were left?"""
    total_water = 24
    water_per_girl = total_water * (1/6)
    water_left_after_girls = total_water - (2 * water_per_girl)
    water_left = water_left_after_girls - 6
    result = water_left
    return result

print(solution())