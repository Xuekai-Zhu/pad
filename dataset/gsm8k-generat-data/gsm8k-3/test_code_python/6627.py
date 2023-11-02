def solution():
    """John has been having trouble sleeping lately.  In the past week he was only able to get 3 hours of sleep on 2 of the days and on the remaining days he was only able to get 60% of the recommended 8 hours of sleep.  How much sleep did he get this week?"""
    # Calculate the total hours of sleep for the two days where John only got 3 hours
    total_3_hour_days = 2
    hours_of_sleep_3_hour_days = total_3_hour_days * 3

    # Calculate the total hours of sleep for the remaining days
    remaining_days = 7 - total_3_hour_days
    recommended_hours_of_sleep = 8
    percent_of_recommended_sleep = 0.6
    hours_of_sleep_remaining_days = remaining_days * recommended_hours_of_sleep * percent_of_recommended_sleep

    # Calculate the total hours of sleep for the week
    total_hours_of_sleep = hours_of_sleep_3_hour_days + hours_of_sleep_remaining_days

    # Display the total hours of sleep for the week
    result = total_hours_of_sleep
    return result

print(solution())