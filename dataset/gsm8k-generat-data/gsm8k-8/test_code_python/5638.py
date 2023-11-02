def solution():
    # Define the number of weekdays and weekends
    weekdays = 5
    weekends = 2

    # Define Janna's sleep hours per day
    weekday_sleep = 7
    weekend_sleep = 8

    # Calculate the total sleep hours per week
    total_sleep = weekdays * weekday_sleep + weekends * weekend_sleep
    result = total_sleep
    return result

print(solution())