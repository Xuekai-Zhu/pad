def solution():
    """Jacob's water tank can hold up to 50 liters of water. Jacob collects water from the river and rain to fill his water tank. He can collect 800 milliliters of water from the rain and 1700 milliliters of water from the river every day. How many days does Jacob need to fill up his water tank?"""
    tank_size = 50
    rain_water = 0.8 # liters
    river_water = 1.7 # liters
    daily_water = rain_water + river_water
    days_to_fill = tank_size / daily_water
    result = days_to_fill
    return result

print(solution())