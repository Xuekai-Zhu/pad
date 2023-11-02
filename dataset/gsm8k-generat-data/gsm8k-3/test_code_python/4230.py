def solution():
    """Claudia has 122 ounces of water and is filling up cups. She has 8-ounce glasses, 5-ounce glasses, and 4-ounce glasses. If she fills six 5 ounce glasses and four 8 ounce glasses, how many 4 ounce glasses can she fill with the remaining water?"""
    # Define the amount of water Claudia has
    water = 122

    # Calculate the total amount of water used for the 6 5-ounce glasses
    five_oz_total = 6 * 5

    # Calculate the total amount of water used for the 4 8-ounce glasses
    eight_oz_total = 4 * 8

    # Calculate the remaining amount of water
    remaining_water = water - (five_oz_total + eight_oz_total)

    # Calculate the number of 4-ounce glasses that can be filled with the remaining water
    four_oz_glasses = remaining_water // 4

    # Display the number of 4-ounce glasses
    result = four_oz_glasses
    return result

print(solution())