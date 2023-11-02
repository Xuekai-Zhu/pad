def solution():
    
    wall1_area = 3 * 2
    wall2_area = 3 * 2
    wall3_area = 5 * 2
    wall4_area = 4 * 2
    total_area = wall1_area + wall2_area + wall3_area + wall4_area
    cans_of_paint = total_area / 2
    result = cans_of_paint
    return result

print(solution())