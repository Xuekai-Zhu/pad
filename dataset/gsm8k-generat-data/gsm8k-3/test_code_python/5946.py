def solution():
    """Wallace's water heater is twice the size of Catherine's water heater. If the capacity of Wallace's water heater is 40 gallons and it's 3/4 full, calculate the total number of gallons of water they both have if Catherine's water heater is also full with water to 3/4 of its capacity."""
    # Calculate the capacity of Catherine's water heater
    catherine_capacity = 40 / 2 # Wallace's is twice the size

    # Calculate the amount of water in Wallace's water heater
    wallace_water = 40 * 3/4

    # Calculate the amount of water in Catherine's water heater
    catherine_water = catherine_capacity * 3/4

    # Calculate the total amount of water they both have
    total_water = wallace_water + catherine_water

    # Display the total amount of water
    result = total_water
    return result

print(solution())