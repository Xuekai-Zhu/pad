def solution():
    """Mason is a caterer packing up silverware and plates for a big corporate event. Each piece of silverware weighs 4 ounces, and there are three pieces of silverware per setting. Each plate weighs 12 ounces, and there are two plates per setting. If Mason needs enough settings for 15 tables with 8 settings each, plus 20 backup settings in case of breakage, how many ounces will all the settings weigh?"""
    silverware_weight = 4
    silverware_per_setting = 3
    plate_weight = 12
    plates_per_setting = 2
    total_settings = 15 * 8 + 20
    total_silverware_weight = silverware_weight * silverware_per_setting * total_settings
    total_plate_weight = plate_weight * plates_per_setting * total_settings
    total_weight = total_silverware_weight + total_plate_weight
    result = total_weight
    return result

print(solution())