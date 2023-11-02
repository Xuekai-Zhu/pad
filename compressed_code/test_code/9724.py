def solution():
    
    initial_data_points = 200
    added_data_points = initial_data_points * 0.2
    total_data_points = initial_data_points + added_data_points
    reduced_data_points = total_data_points * 0.25
    final_data_points = total_data_points - reduced_data_points
    result = final_data_points
    return result

print(solution())