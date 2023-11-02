def solution():
    units_per_first_floor = 2  # The first floor has 2 apartment units
    units_per_other_floor = 5  # The rest of the floors have 5 apartment units each
    total_floors = 4  # Each building has 4 floors
    total_buildings = 2  # Mr. Resty has 2 identical buildings

    # Calculate the total number of apartment units in one building
    units_per_building = units_per_first_floor + (units_per_other_floor * (total_floors - 1))

    # Calculate the total number of apartment units in both buildings
    total_units = units_per_building * total_buildings
    result = total_units
    return result

print(solution())