def solution():
    
    silverware_weight = 4
    silverware_per_setting = 3
    plate_weight = 12
    plates_per_setting = 2
    total_settings = (15 * 8) + 20
    total_silverware_weight = silverware_weight * silverware_per_setting * total_settings
    total_plate_weight = plate_weight * plates_per_setting * total_settings
    total_weight = total_silverware_weight + total_plate_weight
    result = total_weight
    return result

print(solution())