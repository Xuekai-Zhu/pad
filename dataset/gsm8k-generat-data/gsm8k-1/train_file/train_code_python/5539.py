def solution():
    """Mary, Edna, and Lucy are athletes who train every Saturday. Mary ran 3/8 of a 24-kilometer field on one Saturday. Edna ran 2/3 of the distance of Edna, and Lucy ran 5/6 of the distance of Edna. How many more kilometers should Lucy run to cover the same distance as Mary?"""
    mary_distance = (3/8) * 24
    edna_distance = (2/3) * mary_distance
    lucy_distance = (5/6) * edna_distance
    extra_distance = mary_distance - lucy_distance
    result = extra_distance
    return result

print(solution())