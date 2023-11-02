def solution():
    # Calculate the number of data points after adding 20%
    increased_data_points = 200 * (1 + 0.20)

    # Calculate the number of data points after reducing by 1/4
    final_data_points = increased_data_points * (1 - 1/4)
    result = final_data_points
    return result

print(solution())