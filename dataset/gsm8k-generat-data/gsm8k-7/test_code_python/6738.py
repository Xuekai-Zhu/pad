def solution():
    primary_tank_hours = 2
    supplemental_tank_hours = 1
    total_hours_needed = 8

    # Calculate the number of hours of diving time Beth has with just the primary tank
    primary_tank_diving_time = primary_tank_hours

    # Calculate the number of hours of diving time needed with supplemental tanks
    supplemental_tank_diving_time = total_hours_needed - primary_tank_hours

    # Calculate the number of supplemental tanks needed
    num_supplemental_tanks_needed = supplemental_tank_diving_time / supplemental_tank_hours
    result = num_supplemental_tanks_needed
    return result

print(solution())