def solution():
    """Mason is a caterer packing up silverware and plates for a big corporate event. Each piece of silverware weighs 4 ounces, and there are three pieces of silverware per setting. Each plate weighs 12 ounces, and there are two plates per setting. If Mason needs enough settings for 15 tables with 8 settings each, plus 20 backup settings in case of breakage, how many ounces will all the settings weigh?"""
    # Define the weight of each piece of silverware and plate
    silverware_weight = 4  # in ounces
    plate_weight = 12  # in ounces

    # Define the number of pieces of silverware and plates per setting
    silverware_per_setting = 3
    plates_per_setting = 2

    # Define the number of tables and settings
    num_tables = 15
    settings_per_table = 8

    # Calculate the total number of settings, including backup settings
    total_settings = (num_tables * settings_per_table) + 20

    # Calculate the total weight of the silverware and plates for all settings
    total_silverware_weight = silverware_weight * silverware_per_setting * total_settings
    total_plate_weight = plate_weight * plates_per_setting * total_settings
    total_weight = total_silverware_weight + total_plate_weight

    # Return the result in ounces
    result = total_weight
    return result

print(solution())