def solution():
    # Calculate the total amount of water already used
    used_water = 6*5 + 4*8  # six 5 ounce glasses and four 8 ounce glasses filled up
    
    # Calculate the remaining water
    remaining_water = 122 - used_water
    
    # Calculate the number of 4-ounce glasses that can be filled with the remaining water
    num_4_ounce_glasses = remaining_water // 4
    
    result = num_4_ounce_glasses
    return result

print(solution())