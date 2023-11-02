def solution():
    siblings = 4  # Lily has 4 siblings
    siblings_suitcases = 2  # Each sibling is bringing 2 suitcases
    parents_suitcases = 3  # Lily's parents are bringing 3 suitcases

    # Calculate the total number of suitcases
    total_suitcases = (siblings * siblings_suitcases) + (parents_suitcases * 2)
    result = total_suitcases
    return result

print(solution())