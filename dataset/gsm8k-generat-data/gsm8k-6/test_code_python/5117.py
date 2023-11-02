def solution():
    # Calculate the number of apartment units in each building
    first_building = 2 + (5 * 3)  # first floor has 2 units, rest have 5 units each
    second_building = 2 + (5 * 3)

    # Calculate the total number of apartment units in both buildings
    total_units = first_building + second_building
    result = total_units
    return result

print(solution())