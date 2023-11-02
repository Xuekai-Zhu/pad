def solution():
    
    wall_area = 600
    coverage_per_gallon = 400
    total_coverage = wall_area * 2
    cans_of_paint = total_coverage / coverage_per_gallon
    result = cans_of_paint
    return result

print(solution())