def solution():
    # Find the total number of carnations in the first two bouquets
    total_carnations = 9 + 14

    # Find the number of carnations in the third bouquet
    third_bouquet = 3 * 12 - total_carnations  # the average of the three bouquets is 12
    result = third_bouquet
    return result

print(solution())