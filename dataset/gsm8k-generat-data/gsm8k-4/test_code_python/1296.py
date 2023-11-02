def solution():
    """There are 12 carpets in house 1, 20 carpets in house 2, and 10 carpets in house 3. If house 4 has twice as many carpets as house 3, how many carpets do all 4 houses have in total?"""
    # Define the number of carpets in each house
    house1_carpets = 12
    house2_carpets = 20
    house3_carpets = 10
    house4_carpets = house3_carpets * 2

    # Calculate the total number of carpets
    total_carpets = house1_carpets + house2_carpets + house3_carpets + house4_carpets

    # return the result
    result = total_carpets
    return result

print(solution())