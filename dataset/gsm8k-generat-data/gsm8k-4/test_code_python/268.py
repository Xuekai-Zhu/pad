def solution():
    """Trevor buys several bouquets of carnations. The first included 9 carnations; the second included 14 carnations; the third included 13 carnations. What is the average number of carnations in the bouquets?"""
    # Define the number of carnations in each bouquet
    carnations_1 = 9
    carnations_2 = 14
    carnations_3 = 13

    # Calculate the total number of carnations
    total_carnations = carnations_1 + carnations_2 + carnations_3

    # Calculate the average number of carnations
    average_carnations = total_carnations / 3

    result = average_carnations
    return result

print(solution())