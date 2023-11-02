def solution():
    # Constants
    SILVERWARE_WEIGHT_PER_PIECE = 4 # in ounces
    PLATE_WEIGHT = 12 # in ounces
    SILVERWARE_PER_SETTING = 3
    PLATES_PER_SETTING = 2
    TABLES = 15
    SETTINGS_PER_TABLE = 8
    BACKUP_SETTINGS = 20

    # Calculate the total number of settings needed
    total_settings = (TABLES * SETTINGS_PER_TABLE) + BACKUP_SETTINGS

    # Calculate the total weight of all silverware
    total_silverware_weight = SILVERWARE_WEIGHT_PER_PIECE * SILVERWARE_PER_SETTING * total_settings

    # Calculate the total weight of all plates
    total_plate_weight = PLATE_WEIGHT * PLATES_PER_SETTING * total_settings

    # Calculate the total weight of all settings
    total_weight = total_silverware_weight + total_plate_weight
    result = total_weight
    return result

print(solution())