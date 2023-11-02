def solution():
    """Wallace's water heater is twice the size of Catherine's water heater. If the capacity of Wallace's water heater 
    is 40 gallons and it's 3/4 full, calculate the total number of gallons of water they both have if Catherine's water 
    heater is also full with water to 3/4 of its capacity."""
    wallace_capacity = 40
    wallace_level = 3/4
    catherine_capacity = wallace_capacity / 2
    catherine_level = 3/4
    total_gallons = wallace_capacity * wallace_level + catherine_capacity * catherine_level
    result = total_gallons
    return result

print(solution())