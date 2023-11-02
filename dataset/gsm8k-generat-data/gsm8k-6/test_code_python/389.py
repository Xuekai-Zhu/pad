def solution():
    # Calculate the rainfall for the first 15 days of November
    rainfall_first_half = 4 * 15  # 4 inches per day for 15 days

    # Calculate the average daily rainfall for the second half of November
    avg_rainfall_second_half = 2 * 4  # twice the amount observed during the first 15 days

    # Calculate the rainfall for the second half of November
    rainfall_second_half = avg_rainfall_second_half * 15  # average daily rainfall multiplied by the number of days

    # Calculate the total rainfall for the month of November
    total_rainfall = rainfall_first_half + rainfall_second_half

    result = total_rainfall
    return result

print(solution())