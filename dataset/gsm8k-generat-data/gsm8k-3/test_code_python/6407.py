def solution():
    """Carlos bought a box of 50 chocolates. 3 of them were caramels and twice as many were nougats. 
    The number of truffles was equal to the number of caramels plus 6. The rest were peanut clusters. 
    If Carlos picks a chocolate at random, what is the percentage chance it will be a peanut cluster?"""
    # Define the number of caramels and nougats
    caramels = 3
    nougats = 2 * caramels

    # Define the number of truffles
    truffles = caramels + 6

    # Calculate the number of peanut clusters
    peanut_clusters = 50 - caramels - nougats - truffles

    # Calculate the percentage chance of picking a peanut cluster
    percentage = (peanut_clusters / 50) * 100

    # Display the percentage chance
    result = percentage
    return result

print(solution())