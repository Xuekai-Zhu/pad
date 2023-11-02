def solution():
    """Mason is a caterer packing up silverware and plates for a big corporate event. Each piece of silverware weighs 4 ounces, and there are three pieces of silverware per setting. Each plate weighs 12 ounces, and there are two plates per setting. If Mason needs enough settings for 15 tables with 8 settings each, plus 20 backup settings in case of breakage, how many ounces will all the settings weigh?"""
    # Calculate the total number of settings needed
    num_tables = 15
    num_settings_per_table = 8
    num_backup_settings = 20

    total_num_settings = num_tables * num_settings_per_table + num_backup_settings

    # Calculate the total weight of the silverware
    num_silverware_per_setting = 3
    silverware_weight_oz = 4
    total_silverware_weight_oz = total_num_settings * num_silverware_per_setting * silverware_weight_oz

    # Calculate the total weight of the plates
    num_plates_per_setting = 2
    plate_weight_oz = 12
    total_plate_weight_oz = total_num_settings * num_plates_per_setting * plate_weight_oz

    # Calculate the total weight of all the settings
    total_weight_oz = total_silverware_weight_oz + total_plate_weight_oz

    # Display the total weight in ounces
    result = total_weight_oz
    return result

print(solution())