def solution():
    wallace_capacity = 40  # Wallace's water heater has a capacity of 40 gallons
    wallace_full = wallace_capacity * 0.75  # Wallace's water heater is 3/4 full

    # Calculate the capacity of Catherine's water heater
    catherine_capacity = wallace_capacity / 2

    catherine_full = catherine_capacity * 0.75  # Catherine's water heater is also 3/4 full

    # Calculate the total number of gallons of water they both have
    total_water = wallace_full + catherine_full
    result = total_water
    return result

print(solution())