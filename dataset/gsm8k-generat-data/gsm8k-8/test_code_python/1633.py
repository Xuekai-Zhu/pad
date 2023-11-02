def solution():
    # Define the number of chocolates eaten on weekdays and weekends
    weekday_chocolates = 2
    weekend_chocolates = 1

    # Define the total number of chocolates eaten
    total_chocolates = 24

    # Calculate the number of weekdays and weekends
    total_days = 7 * weeks
    weekdays = total_days - weekends
    weekends = total_days - weekdays

    # Calculate the total number of chocolates eaten on weekdays and weekends
    total_weekday_chocolates = weekdays * weekday_chocolates
    total_weekend_chocolates = weekends * weekend_chocolates

    # Calculate the total number of weeks it took to finish all the chocolates
    weeks = total_chocolates / (total_weekday_chocolates + total_weekend_chocolates)
    result = weeks
    return result

print(solution())