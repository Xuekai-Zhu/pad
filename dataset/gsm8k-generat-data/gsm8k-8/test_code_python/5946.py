def solution():
    # Calculate the total capacity of Catherine's water heater
    catherine_capacity = (40 / 2) * (4 / 3)

    # Calculate the total number of gallons of water in Catherine's water heater
    catherine_gallons = catherine_capacity * (3 / 4)

    # Calculate the total number of gallons of water in Wallace's water heater
    wallace_gallons = 40 * (3 / 4)

    # Calculate the total number of gallons of water they both have
    total_gallons = catherine_gallons + wallace_gallons
    result = total_gallons
    return result

print(solution())