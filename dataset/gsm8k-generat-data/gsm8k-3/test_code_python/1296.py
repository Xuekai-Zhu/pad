def solution():
    """There are 12 carpets in house 1, 20 carpets in house 2, and 10 carpets in house 3. If house 4 has twice as many carpets as house 3, how many carpets do all 4 houses have in total?"""
    # Define the number of carpets for each house
    carpets_1 = 12
    carpets_2 = 20
    carpets_3 = 10
    carpets_4 = carpets_3 * 2

    # Calculate the total number of carpets
    total_carpets = carpets_1 + carpets_2 + carpets_3 + carpets_4

    # Display the total number of carpets
    result = total_carpets
    return result

print(solution())