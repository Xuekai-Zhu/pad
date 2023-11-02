def solution():
    # Calculate the number of nougats
    nougats = 2 * 3

    # Calculate the number of truffles
    truffles = 3 + 6

    # Calculate the number of peanut clusters
    peanut_clusters = 50 - (3 + nougats + truffles)

    # Calculate the percentage chance of picking a peanut cluster
    chance = (peanut_clusters / 50) * 100
    result = chance
    return result

print(solution())