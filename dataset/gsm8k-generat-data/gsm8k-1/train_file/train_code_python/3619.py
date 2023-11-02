def solution():
    """The gauge on a water tank shows that the tank is 1/3 full of water. To fill the tank, 16 gallons of water are added. How many gallons of water does the tank hold when full?"""
    tank_fraction_filled = 1/3
    added_water = 16
    tank_capacity = added_water / (1 - tank_fraction_filled)
    result = tank_capacity
    return result

print(solution())