def solution():
    """Joe had 200 data points on his dataset. He then added 20% more data points to the dataset. If he reduced the data points by 1/4 of the total data points, calculate the total number of data points the dataset contains."""
    # Define the initial number of data points
    initial_data_points = 200

    # Calculate the number of data points added
    added_data_points = initial_data_points * 0.2

    # Calculate the total number of data points after adding
    total_data_points = initial_data_points + added_data_points

    # Calculate the number of data points reduced
    reduced_data_points = total_data_points / 4

    # Calculate the final number of data points
    final_data_points = total_data_points - reduced_data_points

    # return the result
    result = final_data_points
    return result

print(solution())