def solution():
    
    total_area = 5040
    known_area = 20 * (8*4)
    remaining_units = 42 - 20
    remaining_area = total_area - known_area
    area_per_unit = remaining_area / remaining_units
    result = area_per_unit
    return result

print(solution())