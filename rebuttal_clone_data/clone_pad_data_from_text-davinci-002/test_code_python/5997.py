def solution():
    silverware_per_setting = 3
    silverware_weight = 4
    plate_per_setting = 2
    plate_weight = 12
    table_settings = 15 * 8
    backup_settings = 20
    all_settings = table_settings + backup_settings
    silverware_weight = all_settings * silverware_per_setting * silverware_weight
    plate_weight = all_settings * plate_per_setting * plate_weight
    total_weight = silverware_weight + plate_weight
    result = total_weight
    return result

print(solution())