def solution():
    
    total_area = 200
    area_covered_by_three_paintings = 3 * 25
    area_covered_by_one_painting = 10 * 8
    remaining_area = total_area - area_covered_by_three_paintings - area_covered_by_one_painting
    width_of_final_painting = remaining_area / 5
    result = width_of_final_painting
    return result

print(solution())