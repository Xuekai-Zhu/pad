def solution():
    customers_per_hour = 175  # Number of customers entering the store every hour
    holiday_season_multiplier = 2  # During the holiday season, the number of customers doubles
    holiday_season_hours = 8  # Number of hours during the holiday season

    # Calculate the total number of customers during the holiday season
    total_customers = customers_per_hour * holiday_season_multiplier * holiday_season_hours
    result = total_customers
    return result

print(solution())