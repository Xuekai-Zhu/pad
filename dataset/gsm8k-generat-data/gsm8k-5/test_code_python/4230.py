def solution():
    total_water = 122  # Claudia has 122 ounces of water
    used_water = (6 * 5) + (4 * 8)  # Claudia has used this much water for the glasses she already filled
    remaining_water = total_water - used_water  # Claudia has this much water left to fill more glasses

    # Calculate how many 4-ounce glasses Claudia can fill with the remaining water
    remaining_glasses = remaining_water // 4
    result = remaining_glasses
    return result

print(solution())