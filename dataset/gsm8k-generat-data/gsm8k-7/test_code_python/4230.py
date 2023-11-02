def solution():
    total_water = 122
    five_ounce_glasses_filled = 6
    eight_ounce_glasses_filled = 4

    # Calculate the total amount of water used to fill the 5-ounce glasses and 8-ounce glasses
    total_used_water = (five_ounce_glasses_filled * 5) + (eight_ounce_glasses_filled * 8)

    # Calculate the remaining water
    remaining_water = total_water - total_used_water

    # Calculate the number of 4-ounce glasses that can be filled with the remaining water
    num_four_ounce_glasses = remaining_water // 4

    result = num_four_ounce_glasses
    return result

print(solution())