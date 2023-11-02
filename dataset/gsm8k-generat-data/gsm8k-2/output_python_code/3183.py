def solution():
    """On our last vacation, I bought 4 times as many tetras as Tim bought clowns.
    Tim bought twice as many clowns as Rick bought guppies. If Rick bought 30 guppies,
    how many animals did we buy on our last vacation?"""
    rick_guppies = 30
    tim_clowns = 2 * rick_guppies
    my_tetras = 4 * tim_clowns
    total_animals = rick_guppies + tim_clowns + my_tetras
    result = total_animals
    return result

print(solution())