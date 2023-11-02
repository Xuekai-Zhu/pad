def solution():
    """Joe had 200 data points on his dataset. He then added 20% more data points to the dataset. If he reduced the data points by 1/4 of the total data points, calculate the total number of data points the dataset contains."""
    # Define the initial number of data points and the percentage increase
    initial_data_points = 200
    percentage_increase = 0.2

    # Calculate the number of data points added
    data_points_added = initial_data_points * percentage_increase

    # Calculate the total number of data points after adding the new ones
    total_data_points = initial_data_points + data_points_added

    # Calculate the number of data points removed
    data_points_removed = total_data_points * (1/4)

    # Calculate the final number of data points
    final_data_points = total_data_points - data_points_removed

    # Display the final number of data points
    result = final_data_points
    return result

print(solution())