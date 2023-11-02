def solution():
    """Carlos bought a box of 50 chocolates. 3 of them were caramels and twice as many were nougats. The number of truffles was equal to the number of caramels plus 6. The rest of the chocolates were peanut clusters. If Carlos picks a chocolate at random, what is the percentage chance it will be a peanut cluster?"""
    chocolates_total = 50
    caramels = 3
    nougats = caramels * 2
    truffles = caramels + 6
    peanut_clusters = chocolates_total - caramels - nougats - truffles
    probability = (peanut_clusters / chocolates_total) * 100
    result = probability
    return result

print(solution())