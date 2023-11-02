def solution():
    """Daleyza won a house construction project that involved the construction of three houses with several units. The first building was designed to have 4000 units, the second building 2/5 times as many units as the first building, and the third building was to have 20% more units than the second building. How many units were Daleyza contracted to build?"""
    # Define the number of units in the first building
    first_building = 4000

    # Calculate the number of units in the second building
    second_building = (2/5) * first_building

    # Calculate the number of units in the third building
    third_building = second_building * 1.2

    # Calculate the total number of units for all three buildings
    total_units = first_building + second_building + third_building

    # Display the total number of units
    result = total_units
    return result

print(solution())