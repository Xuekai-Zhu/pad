def solution():
    
    current_average = (85 + 79 + 92 + 84) / 4
    target_average = 85
    total_points_needed = 5 * target_average - 4 * current_average
    points_needed_on_final_test = total_points_needed
    result = points_needed_on_final_test
    return result

print(solution())