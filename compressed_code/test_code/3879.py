def solution():
    
    original_data_points = 200
    added_data_points = 0.2 * original_data_points
    total_data_points = original_data_points + added_data_points
    reduced_data_points = 0.25 * total_data_points
    remaining_data_points = total_data_points - reduced_data_points
    result = remaining_data_points
    return result

print(solution())