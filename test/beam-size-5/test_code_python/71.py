def solution():
    
    top_level_area = 16
    first_level_area = top_level_area / 2
    second_level_area = first_level_area / 2
    third_level_area = second_level_area / 2
    total_area = top_level_area + second_level_area + third_level_area
    average_area = total_area / 4
    result = average_area
    return result

print(solution())