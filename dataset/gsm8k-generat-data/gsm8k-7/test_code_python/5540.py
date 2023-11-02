def solution():
    mary_distance = (3/8) * 24
    edna_distance = (2/3) * mary_distance
    lucy_distance = (5/6) * edna_distance

    # Calculate how many more kilometers Lucy needs to run to cover the same distance as Mary
    difference = mary_distance - lucy_distance
    result = difference
    return result

print(solution())