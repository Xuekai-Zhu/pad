def solution():
    # Calculate the number of candies that were sour
    sour_candies = 0.4 * 300  

    # Calculate the number of good candies
    good_candies = 300 - sour_candies  

    # Calculate the number of candies each person gets
    candies_per_person = good_candies / 3  # Henley and her two brothers
    result = candies_per_person
    return result

print(solution())