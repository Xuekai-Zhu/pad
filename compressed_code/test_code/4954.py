def solution():
    
    total_chocolates = 50
    caramels = 3
    nougats = 2 * caramels
    truffles = caramels + 6
    peanut_clusters = total_chocolates - caramels - nougats - truffles
    chance_percent = (peanut_clusters / total_chocolates) * 100
    result = chance_percent
    return result

print(solution())