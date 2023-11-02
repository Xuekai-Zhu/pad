def solution():
    # Calculate the total amount of oil in the cans
    total_oil = 290
    
    # Calculate the amount of oil in the 10 cans that hold 8 liters each
    oil_in_small_cans = 10 * 8
    
    # Calculate the number of remaining cans
    remaining_cans = 24 - 10
    
    # Calculate the total amount of oil in the remaining cans
    oil_in_remaining_cans = total_oil - oil_in_small_cans
    
    # Calculate the amount of oil in each of the remaining cans
    oil_per_remaining_can = oil_in_remaining_cans / remaining_cans
    
    result = oil_per_remaining_can
    return result

print(solution())