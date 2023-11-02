def solution():
    """John has been having trouble sleeping lately. In the past week he was only able to get 3 hours of sleep on 2 of the days and on the remaining days he was only able to get 60% of the recommended 8 hours of sleep. How much sleep did he get this week?"""
    # Define the number of days in the week
    days_in_week = 7

    # Calculate the total recommended sleep for the week
    recommended_sleep = 8 * days_in_week

    # Calculate the total number of hours John was able to sleep on the 2 days
    total_sleep_2_days = 2 * 3

    # Calculate the total number of hours John was able to sleep on the remaining days
    total_sleep_remaining_days = (days_in_week - 2) * 0.6 * 8

    # Calculate the total number of hours John was able to sleep for the week
    total_sleep = total_sleep_2_days + total_sleep_remaining_days

    result = total_sleep
    return result

print(solution())