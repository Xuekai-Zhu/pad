def solution():
    """Joe had 200 data points on his dataset. He then added 20% more data points to the dataset. If he reduced the data points by 1/4 of the total data points, calculate the total number of data points the dataset contains."""
    initial_data_points = 200
    added_data_points = initial_data_points * 0.2
    total_data_points = initial_data_points + added_data_points
    reduced_data_points = total_data_points * 0.25
    final_data_points = total_data_points - reduced_data_points
    result = final_data_points
    return result

print(solution())