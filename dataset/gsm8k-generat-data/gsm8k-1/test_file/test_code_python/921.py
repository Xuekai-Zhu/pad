def solution():
    """There are 10000 gallons of water in a pool. Using a water pump, Anthony and his father fill a tank with half the amount of water in the pool. They use water from the tank to water their vegetable garden. If the tank is emptied at a rate of 500 gallons of water per day, how many gallons of water will be remaining in the tank after 6 days?"""
    pool_water = 10000
    tank_water = pool_water / 2
    water_used = 500 * 6
    remaining_water = tank_water - water_used
    result = remaining_water
    return result

print(solution())