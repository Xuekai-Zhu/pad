def solution():
    """A water tank is filled with 120 liters of water. Celine used 90 liters of water from the tank to water her small garden. She was then able to collect rainwater that is twice as much as what was left. How many liters of water are in the tank now?"""
    initial_water = 120
    water_used = 90
    water_left = initial_water - water_used
    collected_rainwater = water_left * 2
    total_water = collected_rainwater + water_left
    result = total_water
    return result

print(solution())