def solution():
    
    wall1_area = 3 * 2
    wall2_area = 3 * 2
    wall3_area = 5 * 2
    wall4_area = 4 * 2
    total_area = wall1_area + wall2_area + wall3_area + wall4_area
    cans_needed = total_area / 2
    result = cans_needed
    return result

print(solution())