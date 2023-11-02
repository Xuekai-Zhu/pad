def solution():
    """Jacob's water tank can hold up to 50 liters of water. Jacob collects water from the river and rain to fill his water tank. He can collect 800 milliliters of water from the rain and 1700 milliliters of water from the river every day. How many days does Jacob need to fill up his water tank?"""
    tank_capacity = 50 * 1000 # convert liters to milliliters
    rain_collect = 800
    river_collect = 1700
    total_collect_per_day = rain_collect + river_collect
    days_to_fill_tank = tank_capacity // total_collect_per_day
    result = days_to_fill_tank
    return result

print(solution())