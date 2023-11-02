def solution():
    # Calculate the weight of silverware and plates per setting
    weight_per_setting = 3*4 + 2*12  # 3 pieces of silverware at 4 oz each, and 2 plates at 12 oz each

    # Calculate the total number of settings needed
    total_settings = 15*8 + 20  # 15 tables with 8 settings each, plus 20 backup settings

    # Calculate the total weight of all the settings
    total_weight = total_settings * weight_per_setting
    
    result = total_weight
    return result

print(solution())