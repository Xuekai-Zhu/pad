def solution():
    
    total_floors = 23
    regular_floors = total_floors - 2
    regular_units_per_floor = 12
    penthouse_units_per_floor = 2
    regular_units = regular_floors * regular_units_per_floor
    penthouse_units = 2 * penthouse_units_per_floor
    total_units = regular_units + penthouse_units
    result = total_units
    return result

print(solution())