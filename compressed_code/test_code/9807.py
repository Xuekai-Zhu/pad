def solution():
    
    floors_per_building = 4
    units_on_first_floor = 2
    units_per_floor = 5
    total_units_per_building = (floors_per_building - 1) * units_per_floor + units_on_first_floor
    total_units = total_units_per_building * 2
    result = total_units
    return result

print(solution())