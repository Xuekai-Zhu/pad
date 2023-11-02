def solution():
    """Trevor buys three bouquets of carnations. The first included 9 carnations, and the second included 14 carnations. If the average number of carnations in the bouquets is 12, how many carnations were in the third bouquet?"""
    # Define the total number of carnations and the number of bouquets
    total_carnations = 0
    num_bouquets = 3

    # Define the number of carnations in the first two bouquets
    carnations_1 = 9
    carnations_2 = 14

    # Calculate the total number of carnations
    total_carnations = (num_bouquets * 12) - (carnations_1 + carnations_2)

    # Calculate the number of carnations in the third bouquet
    carnations_3 = total_carnations

    # return the result
    result = carnations_3
    return result

print(solution())