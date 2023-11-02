def solution():
    """Carlos bought a box of 50 chocolates. 3 of them were caramels and twice as many were nougats. The number of truffles was equal to the number of caramels plus 6. The rest of the chocolates were peanut clusters. If Carlos picks a chocolate at random, what is the percentage chance it will be a peanut cluster?"""
    total_chocolates = 50
    caramels = 3
    nougats = 2 * caramels
    truffles = caramels + 6
    peanut_clusters = total_chocolates - caramels - nougats - truffles
    chance_percent = (peanut_clusters / total_chocolates) * 100
    result = chance_percent
    return result

print(solution())