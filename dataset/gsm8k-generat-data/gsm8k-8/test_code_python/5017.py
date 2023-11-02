def solution():
    # Define the initial number of data points
    initial_data_points = 200

    # Calculate the number of additional data points
    additional_data_points = 0.2 * initial_data_points

    # Calculate the total number of data points after adding the additional ones
    total_data_points = initial_data_points + additional_data_points

    # Calculate the number of data points to be removed
    removed_data_points = total_data_points / 4

    # Calculate the final number of data points in the dataset
    final_data_points = total_data_points - removed_data_points
    result = final_data_points
    return result

print(solution())