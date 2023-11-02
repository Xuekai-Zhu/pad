def solution():
    data_points = 200
    added_data_points = data_points * .2
    new_data_points = data_points + added_data_points
    reduced_data_points = new_data_points / 4
    total_data_points = new_data_points - reduced_data_points
    result = total_data_points
    
    return result

print(solution())