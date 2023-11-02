def solution():
    wallace_capacity = 40
    wallace_fullness = 3/4
    catherine_capacity = wallace_capacity / 2  # given that Wallace's water heater is twice the size of Catherine's
    catherine_fullness = 3/4

    # Calculate the total gallons of water in Wallace's water heater
    wallace_gallons = wallace_capacity * wallace_fullness

    # Calculate the total gallons of water in Catherine's water heater
    catherine_gallons = catherine_capacity * catherine_fullness

    # Calculate the total gallons of water they both have
    total_gallons = wallace_gallons + catherine_gallons
    result = total_gallons
    return result

print(solution())