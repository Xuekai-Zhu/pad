def solution():
    original_data_points = 200  # Joe had 200 data points on his dataset
    added_data_points = int(original_data_points * 0.2)  # Joe added 20% more data points
    total_data_points = original_data_points + added_data_points  # Joe now has a total of (original_data_points + added_data_points) data points
    reduced_data_points = total_data_points // 4  # Joe reduced the data points by 1/4 of the total data points

    # Calculate the final total number of data points
    final_data_points = total_data_points - reduced_data_points
    result = final_data_points
    return result

print(solution())