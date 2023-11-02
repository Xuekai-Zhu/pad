def solution():
    """On our last vacation, I bought 4 times as many tetras as Tim bought clowns. Tim bought twice as many clowns as Rick bought guppies. If Rick bought 30 guppies, how many animals did we buy on our last vacation?"""
    # Define the number of guppies, clowns, and tetras bought
    guppies = 30
    clowns = guppies * 2
    tetras = clowns * 4

    # Calculate the total number of animals bought
    total_animals = guppies + clowns + tetras

    # return the result
    result = total_animals
    return result

print(solution())