def solution():
    
    wall_area = 600
    coverage_per_gallon = 400
    total_coverage_needed = wall_area * 2
    gallons_needed = total_coverage_needed / coverage_per_gallon
    result = gallons_needed
    return result

print(solution())