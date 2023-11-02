def solution():
    # Define the weight of one setting
    weight_per_setting = 3 * 4 + 2 * 12

    # Calculate the total number of settings needed
    total_settings = 15 * 8 + 20

    # Calculate the total weight of all the settings
    total_weight = total_settings * weight_per_setting
    result = total_weight
    return result

print(solution())