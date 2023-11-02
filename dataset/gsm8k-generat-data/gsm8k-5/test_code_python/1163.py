def solution():
    total_carnations = 3 * 12  # The total number of carnations in all three bouquets is 3 times the average
    carnations_in_first_two_bouquets = 9 + 14  # The total number of carnations in the first two bouquets

    # Calculate the number of carnations in the third bouquet
    carnations_in_third_bouquet = total_carnations - carnations_in_first_two_bouquets
    result = carnations_in_third_bouquet
    return result

print(solution())