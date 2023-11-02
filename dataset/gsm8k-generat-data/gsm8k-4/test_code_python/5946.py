def solution():
    """Wallace's water heater is twice the size of Catherine's water heater. If the capacity of Wallace's water heater is 40 gallons and it's 3/4 full, calculate the total number of gallons of water they both have if Catherine's water heater is also full with water to 3/4 of its capacity."""
    # Define the size of Wallace's water heater
    wallace_size = 40

    # Calculate the amount of water in Wallace's water heater
    wallace_water = wallace_size * 0.75

    # Calculate the size of Catherine's water heater
    catherine_size = wallace_size / 2

    # Calculate the amount of water Catherine's water heater can hold
    catherine_water = catherine_size * 0.75

    # Calculate the total amount of water they both have
    total_water = wallace_water + catherine_water

    # Return the result
    result = total_water
    return result

print(solution())