def solution():
    # Calculate the total number of nougats and caramels
    nougats = 2 * 3
    caramels = 3
    
    # Calculate the number of truffles
    truffles = caramels + 6
    
    # Calculate the number of peanut clusters
    peanut_clusters = 50 - nougats - caramels - truffles
    
    # Calculate the percentage chance of picking a peanut cluster
    percentage_peanut_clusters = (peanut_clusters / 50) * 100
    result = percentage_peanut_clusters
    return result

print(solution())