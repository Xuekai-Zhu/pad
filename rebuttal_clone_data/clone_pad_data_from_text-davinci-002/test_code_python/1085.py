def solution():
    siblings = 4
    suitcases_per_sibling = 2
    parents = 2
    suitcases_per_parent = 3
    total_suitcases = siblings * suitcases_per_sibling + parents * suitcases_per_parent
    result = total_suitcases
    return result

print(solution())