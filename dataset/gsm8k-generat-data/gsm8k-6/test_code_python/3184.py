def solution():
    # Find how many clowns Tim bought
    clowns_Tim = 2 * 30  # Tim bought twice as many clowns as Rick bought guppies

    # Find how many tetras were bought by "I"
    tetras_I = 4 * clowns_Tim  # "I" bought 4 times as many tetras as Tim bought clowns

    # Calculate the total number of animals bought
    total_animals = 30 + clowns_Tim + tetras_I  # Rick bought 30 guppies
    result = total_animals
    return result

print(solution())