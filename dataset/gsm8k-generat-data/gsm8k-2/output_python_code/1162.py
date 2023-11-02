def solution():
    """Trevor buys three bouquets of carnations. The first included 9 carnations, and the second included 14 carnations. If the average number of carnations in the bouquets is 12, how many carnations were in the third bouquet?"""
    total_carnations = 3 * 12
    third_bouquet_carnations = total_carnations - 9 - 14
    result = third_bouquet_carnations
    return result

print(solution())