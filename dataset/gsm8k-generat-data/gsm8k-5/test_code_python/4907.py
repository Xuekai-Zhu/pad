def solution():
    # Units in first building
    units_building1 = 4000

    # Units in second building, which is 2/5 times as many as the first building
    units_building2 = (2/5) * units_building1

    # Units in third building, which is 20% more than the units in the second building
    units_building3 = units_building2 * 1.2

    # Total units contracted to build
    total_units = units_building1 + units_building2 + units_building3
    result = total_units
    return result

print(solution())