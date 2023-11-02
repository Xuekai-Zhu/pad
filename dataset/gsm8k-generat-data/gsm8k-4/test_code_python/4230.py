def solution():
    """Claudia has 122 ounces of water and is filling up cups. She has 8-ounce glasses, 5-ounce glasses, and 4-ounce glasses. If she fills six 5 ounce glasses and four 8 ounce glasses, how many 4 ounce glasses can she fill with the remaining water?"""
    # Define the amount of water Claudia has
    total_water = 122

    # Define the amount of water used for 6 5-ounce glasses and 4 8-ounce glasses
    used_water = (6 * 5) + (4 * 8)

    # Calculate the remaining water
    remaining_water = total_water - used_water

    # Calculate the number of 4-ounce glasses that can be filled with the remaining water
    num_4oz_glasses = remaining_water // 4

    # Return the result
    result = num_4oz_glasses
    return result

print(solution())