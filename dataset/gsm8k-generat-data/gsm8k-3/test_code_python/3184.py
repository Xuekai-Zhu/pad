def solution():
    """On our last vacation, I bought 4 times as many tetras as Tim bought clowns. Tim bought twice as many clowns as Rick bought guppies. If Rick bought 30 guppies, how many animals did we buy on our last vacation?"""
    # Define the number of guppies that Rick bought
    guppies = 30

    # Calculate the number of clowns Tim bought
    clowns = 2 * guppies

    # Calculate the number of tetras I bought
    tetras = 4 * clowns

    # Calculate the total number of animals bought
    total_animals = guppies + clowns + tetras

    # Display the total number of animals bought
    result = total_animals
    return result

print(solution())