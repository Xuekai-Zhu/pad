def solution():
    """Daleyza won a house construction project that involved the construction of three houses with several units. The first building was designed to have 4000 units, the second building 2/5 times as many units as the first building, and the third building was to have 20% more units than the second building. How many units were Daleyza contracted to build?"""
    first_building_units = 4000
    second_building_units = (2/5) * first_building_units
    third_building_units = 1.2 * second_building_units
    total_units = first_building_units + second_building_units + third_building_units
    result = total_units
    return result

print(solution())