def solution():
    # Calculate the time to saute the garlic and peppers
    saute_garlic_and_peppers_time = 0.25 * 20

    # Calculate the time to knead and rest the dough
    knead_time = 30
    rest_time = 2 * knead_time
    knead_and_rest_time = knead_time + rest_time

    # Calculate the time to assemble the calzones
    assembly_time = 0.1 * knead_and_rest_time

    # Calculate the total time spent on the calzones
    total_time = 20 + saute_garlic_and_peppers_time + knead_and_rest_time + assembly_time
    result = total_time
    return result

print(solution())