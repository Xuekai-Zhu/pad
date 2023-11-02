def solution():
    """Trevor buys three bouquets of carnations. The first included 9 carnations, and the second included 14 carnations. If the average number of carnations in the bouquets is 12, how many carnations were in the third bouquet?"""
    # Calculate the total number of carnations in the first two bouquets
    total_carnations = 9 + 14

    # Calculate the number of carnations in the third bouquet
    third_bouquet = 3 * 12 - total_carnations

    # Display the number of carnations in the third bouquet
    result = third_bouquet
    return result

print(solution())