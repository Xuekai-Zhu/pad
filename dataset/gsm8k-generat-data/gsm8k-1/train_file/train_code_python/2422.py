def solution():
    """Rory collects rainwater. He has 100 L of rainwater in his tank. During a heavy rainstorm, water flows into the tank at a rate of 2 L/min for 90 minutes. How much water is in the tank at the end of the heavy rain?"""
    initial_water = 100
    water_added = 2 * 90
    total_water = initial_water + water_added
    result = total_water
    return result

print(solution())