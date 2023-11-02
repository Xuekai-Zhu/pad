def solution():
    mary_distance = 3/8 * 24
    edna_distance = 2/3 * mary_distance
    lucy_distance = 5/6 * edna_distance
    lucy_extra_distance = mary_distance - lucy_distance
    result = lucy_extra_distance
    return result

print(solution())