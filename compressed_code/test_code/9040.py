def solution():
    
    total_area = 5040
    known_units = 20
    known_area = 8 * 4 * known_units
    remaining_area = total_area - known_area
    remaining_units = 42 - known_units
    area_per_unit = remaining_area / remaining_units
    result = area_per_unit
    return result

print(solution())