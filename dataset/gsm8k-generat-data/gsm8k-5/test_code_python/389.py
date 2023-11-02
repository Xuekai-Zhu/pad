def solution():
    # Calculate the total rainfall for the first 15 days
    rainfall_first_15_days = 4 * 15  # 4 inches per day for 15 days

    # Calculate the average daily rainfall for the remaining days
    average_daily_rainfall = 4 * 2  # Twice the amount observed during the first 15 days

    # Calculate the total rainfall for the remaining days
    remaining_days = 30 - 15  # November has 30 days
    rainfall_remaining_days = average_daily_rainfall * remaining_days

    # Calculate the total rainfall for November
    total_rainfall = rainfall_first_15_days + rainfall_remaining_days
    result = total_rainfall
    return result

print(solution())