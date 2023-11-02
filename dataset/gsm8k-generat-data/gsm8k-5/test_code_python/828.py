def solution():
    # Calculate the total sleep Tim got in the first 2 days
    sleep_first_two_days = 6 + 6  # Tim got 6 hours of sleep each day

    # Calculate the total sleep Tim got in the next 2 days
    sleep_next_two_days = 10 + 10  # Tim got 10 hours of sleep each day

    # Calculate the total sleep Tim got in 4 days
    total_sleep = sleep_first_two_days + sleep_next_two_days
    result = total_sleep
    return result

print(solution())