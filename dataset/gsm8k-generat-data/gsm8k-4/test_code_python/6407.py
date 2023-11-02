def solution():
    """Carlos bought a box of 50 chocolates. 3 of them were caramels and twice as many were nougats. The number of truffles was equal to the number of caramels plus 6. The rest of the chocolates were peanut clusters. If Carlos picks a chocolate at random, what is the percentage chance it will be a peanut cluster?"""
    # Define the total number of chocolates and the number of caramels
    total_chocolates = 50
    caramels = 3

    # Calculate the number of nougats and truffles
    nougats = caramels * 2
    truffles = caramels + 6

    # Calculate the number of peanut clusters
    peanut_clusters = total_chocolates - (caramels + nougats + truffles)

    # Calculate the percentage chance of picking a peanut cluster
    peanut_cluster_percentage = (peanut_clusters / total_chocolates) * 100

    # Return the result
    result = peanut_cluster_percentage
    return result

print(solution())