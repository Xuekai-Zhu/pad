def solution():
    siblings = 4
    siblings_suitcases = 2
    parents_suitcases = 3

    # Calculate the number of suitcases brought by the siblings
    total_siblings_suitcases = siblings * siblings_suitcases

    # Calculate the number of suitcases brought by the parents
    total_parents_suitcases = parents_suitcases * 2

    # Calculate the total number of suitcases brought by the family
    total_suitcases = total_siblings_suitcases + total_parents_suitcases
    result = total_suitcases
    return result

print(solution())