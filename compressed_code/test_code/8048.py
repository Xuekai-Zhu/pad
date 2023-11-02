def solution():
    
    wall_area = 1600
    paint_coverage = 400
    coats_needed = 2
    gallons_needed = wall_area / paint_coverage * coats_needed
    cost_per_person = 45 * gallons_needed / 2
    result = cost_per_person
    return result

print(solution())