def solution():
    """Daleyza won a house construction project that involved the construction of three houses with several units. The first building was designed to have 4000 units, the second building 2/5 times as many units as the first building, and the third building was to have 20% more units than the second building. How many units were Daleyza contracted to build?"""
    # Calculate the number of units in the first building
    building1_units = 4000

    # Calculate the number of units in the second building
    building2_units = (2/5) * building1_units

    # Calculate the number of units in the third building
    building3_units = building2_units * 1.2

    # Calculate the total number of units in all three buildings
    total_units = building1_units + building2_units + building3_units

    # return the result
    result = total_units
    return result

print(solution())