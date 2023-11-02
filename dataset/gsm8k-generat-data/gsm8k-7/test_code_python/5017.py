def solution():
    original_data_points = 200
    additional_data_points = 0.2 * original_data_points

    # Calculate the total number of data points after addition
    total_data_points = original_data_points + additional_data_points

    # Calculate the number of data points to be removed
    removed_data_points = 0.25 * total_data_points

    # Calculate the final number of data points
    final_data_points = total_data_points - removed_data_points
    result = final_data_points
    return result

print(solution())