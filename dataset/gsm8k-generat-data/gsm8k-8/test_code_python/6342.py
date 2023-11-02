def solution():
    # Define the number of people entering the store per hour
    normal_hourly_rate = 175

    # Calculate the number of people entering the store during the holiday season
    holiday_hourly_rate = normal_hourly_rate * 2

    # Calculate the total number of people entering the store during 8 hours
    total_customers_during_holiday_season = holiday_hourly_rate * 8

    result = total_customers_during_holiday_season
    return result

print(solution())