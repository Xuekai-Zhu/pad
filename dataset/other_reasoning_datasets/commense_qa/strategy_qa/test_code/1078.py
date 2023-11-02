def solution():
    has_sufficient_area = False
    has_skis = False
    has_tow_boat = False
    has_people = False
    has_pfd = False
    is_water_present = False
    is_temperature_suitable = False
    
    # Check if all necessary equipment is present
    if has_sufficient_area and has_skis and has_tow_boat and has_people and has_pfd:
        # Check if there is water present on Venus
        if is_water_present:
            # Check if the temperature is suitable for water skiing
            if is_temperature_suitable:
                result = "yes"
            else:
                result = "no"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())