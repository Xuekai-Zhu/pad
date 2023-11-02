def solution():
    
    regular_units_per_floor = 12
    penthouse_units_per_floor = 2
    regular_floors = 21
    penthouse_floors = 2
    total_regular_units = regular_floors * regular_units_per_floor
    total_penthouse_units = penthouse_floors * penthouse_units_per_floor
    total_units = total_regular_units + total_penthouse_units
    result = total_units
    return result

print(solution())