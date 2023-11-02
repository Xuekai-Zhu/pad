def solution():
    """Trevor buys several bouquets of carnations. The first included 9 carnations; the second included 14 carnations; the third included 13 carnations. What is the average number of carnations in the bouquets?"""
    bouquet1 = 9
    bouquet2 = 14
    bouquet3 = 13
    total_carnations = bouquet1 + bouquet2 + bouquet3
    num_bouquets = 3
    average_carnations = total_carnations / num_bouquets
    result = average_carnations
    return result

print(solution())