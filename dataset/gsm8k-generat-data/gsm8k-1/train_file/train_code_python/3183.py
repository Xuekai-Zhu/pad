def solution():
    """On our last vacation, I bought 4 times as many tetras as Tim bought clowns. Tim bought twice as many clowns as Rick bought guppies. If Rick bought 30 guppies, how many animals did we buy on our last vacation?"""
    guppies = 30
    clowns = 2 * guppies
    tetras = 4 * clowns
    total = guppies + clowns + tetras
    result = total
    return result

print(solution())