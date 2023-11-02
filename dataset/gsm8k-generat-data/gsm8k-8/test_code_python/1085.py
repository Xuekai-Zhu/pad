def solution():
    # Define the number of suitcases each sibling is bringing
    sibling_suitcases = 2

    # Calculate the total number of sibling suitcases
    total_sibling_suitcases = sibling_suitcases * 4

    # Define the number of suitcases each parent is bringing
    parent_suitcases = 3

    # Calculate the total number of parent suitcases
    total_parent_suitcases = parent_suitcases * 2

    # Calculate the total number of suitcases
    total_suitcases = total_sibling_suitcases + total_parent_suitcases

    result = total_suitcases
    return result

print(solution())