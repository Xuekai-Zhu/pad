def solution():
    
    primary_tank_hours = 2
    total_hours = 8
    supplemental_tank_hours = 1
    remaining_hours = total_hours - primary_tank_hours
    supplemental_tanks_needed = remaining_hours // supplemental_tank_hours
    if remaining_hours % supplemental_tank_hours != 0:
        supplemental_tanks_needed += 1
    result = supplemental_tanks_needed
    return result

print(solution())