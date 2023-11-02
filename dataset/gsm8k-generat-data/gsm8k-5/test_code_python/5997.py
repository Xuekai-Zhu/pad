def solution():
    # Calculate the weight of the silverware per setting
    weight_silverware = 3 * 4  # 3 pieces of silverware, each weighing 4 ounces

    # Calculate the weight of the plates per setting
    weight_plates = 2 * 12  # 2 plates, each weighing 12 ounces

    # Calculate the total weight per setting
    weight_per_setting = weight_silverware + weight_plates

    # Calculate the total number of settings needed
    total_settings = (15 * 8) + 20  # 15 tables with 8 settings each, plus 20 backups

    # Calculate the total weight of all the settings
    total_weight = total_settings * weight_per_setting
    result = total_weight
    return result

print(solution())