def solution():
    # Define the total number of carnations in the two bouquets
    total_carnations = 9 + 14

    # Define the total number of bouquets
    total_bouquets = 3

    # Calculate the number of carnations in the third bouquet
    third_bouquet = (total_bouquets * 12) - total_carnations
    result = third_bouquet
    return result

print(solution())