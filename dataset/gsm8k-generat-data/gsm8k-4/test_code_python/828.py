def solution():
    """Tim gets 6 hours of sleep 2 days in a row. To make up for it he sleeps 10 hours the next 2 days. How much sleep did he get?"""
    # Calculate the total hours of sleep for the first two days
    sleep_first_two_days = 6 * 2

    # Calculate the total hours of sleep for the next two days
    sleep_next_two_days = 10 * 2

    # Calculate the total hours of sleep for the week
    total_sleep = sleep_first_two_days + sleep_next_two_days

    result = total_sleep
    return result

print(solution())