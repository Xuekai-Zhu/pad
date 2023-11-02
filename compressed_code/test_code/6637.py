def solution():
    
    siblings = 4
    siblings_suitcases = 2
    parents = 2
    parents_suitcases = 3
    total_suitcases = (siblings * siblings_suitcases) + (parents * parents_suitcases)
    result = total_suitcases
    return result

print(solution())