def solution():
    # Calculate the total amount of juice in liters
    total_juice_liters = 5 * 2

    # Calculate the total number of glasses that can be filled
    num_glasses = (total_juice_liters * 1000) // 250  # converting liters to milliliters and integer division to ensure only full glasses are counted
    result = num_glasses
    return result

print(solution())