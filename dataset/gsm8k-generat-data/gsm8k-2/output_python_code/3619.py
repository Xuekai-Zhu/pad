def solution():
    """The gauge on a water tank shows that the tank is 1/3 full of water. To fill the tank, 16 gallons of water are added. How many gallons of water does the tank hold when full?"""
    tank_capacity = 16 / (1 - 1/3)
    result = tank_capacity
    return result

print(solution())