def solution():
    first_15_days_rainfall = 4  # inches per day
    remaining_days = 30 - 15  # number of days left in November
    average_daily_rainfall = 2 * first_15_days_rainfall

    # Calculate the total rainfall for the first 15 days
    total_rainfall_first_15_days = first_15_days_rainfall * 15

    # Calculate the total rainfall for the remaining days
    total_rainfall_remaining_days = average_daily_rainfall * remaining_days

    # Calculate the total rainfall for the entire month
    total_rainfall = total_rainfall_first_15_days + total_rainfall_remaining_days
    result = total_rainfall
    return result

print(solution())