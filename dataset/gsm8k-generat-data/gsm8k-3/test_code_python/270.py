def solution():
    """Trevor buys several bouquets of carnations. The first included 9 carnations; the second included 14 carnations; the third included 13 carnations. What is the average number of carnations in the bouquets?"""
    # Define the number of carnations in each bouquet
    bouquet1 = 9
    bouquet2 = 14
    bouquet3 = 13

    # Calculate the total number of carnations
    total_carnations = bouquet1 + bouquet2 + bouquet3

    # Calculate the average number of carnations
    average_carnations = total_carnations / 3

    # Display the average number of carnations
    result = average_carnations
    return result

print(solution())