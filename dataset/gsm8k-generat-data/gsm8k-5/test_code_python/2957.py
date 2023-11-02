def solution():
    days_with_6_hours = 5  # Tim sleeps 6 hours for 5 days a week
    days_with_10_hours = 2  # Tim sleeps 10 hours for 2 days a week

    # Calculate total sleep for days with 6 hours
    total_sleep_at_6_hours = days_with_6_hours * 6

    # Calculate total sleep for days with 10 hours
    total_sleep_at_10_hours = days_with_10_hours * 10

    # Calculate the total sleep for the week
    total_sleep = total_sleep_at_6_hours + total_sleep_at_10_hours

    result = total_sleep
    return result

print(solution())