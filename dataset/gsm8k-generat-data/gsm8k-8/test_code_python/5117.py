def solution():
    # Calculate the number of apartment units on each floor (excluding the ground floor)
    units_per_floor = 5

    # Calculate the total number of floors in both buildings
    total_floors = 4

    # Calculate the number of apartment units on the ground floor of each building
    ground_floor_units = 2

    # Calculate the total number of units on each building (excluding the ground floor)
    building_units = units_per_floor * (total_floors - 1)

    # Calculate the total number of units in both buildings (excluding the ground floor)
    total_units = building_units * 2

    # Add the number of units on the ground floor of each building
    total_units += ground_floor_units * 2

    result = total_units
    return result

print(solution())