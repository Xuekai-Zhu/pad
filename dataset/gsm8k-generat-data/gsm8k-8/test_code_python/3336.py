def solution():
    # Calculate the total number of wheels from the adults riding bicycles
    adult_wheels = 6 * 2

    # Calculate the total number of wheels from the children riding tricycles
    child_wheels = 15 * 3

    # Calculate the total number of wheels seen by Dimitri
    total_wheels = adult_wheels + child_wheels
    result = total_wheels
    return result

print(solution())