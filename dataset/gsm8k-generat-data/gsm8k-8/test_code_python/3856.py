def solution():
    caps_per_month_first_year = 3
    caps_per_month_after_first_year = 5
    caps_per_christmas = 40
    caps_lost_per_year = 15

    # Calculate caps collected in first year
    caps_first_year = caps_per_month_first_year * 12

    # Calculate caps collected in the following years
    caps_after_first_year = (caps_per_month_after_first_year * 12) * 4

    # Calculate caps received from Christmas
    caps_from_christmas = caps_per_christmas * 5

    # Calculate total caps collected
    total_caps = caps_first_year + caps_after_first_year + caps_from_christmas

    # Calculate caps lost
    caps_lost = caps_lost_per_year * 5
    
    # Calculate caps Lilith currently has
    caps_currently_have = total_caps - caps_lost
    result = caps_currently_have
    return result

print(solution())