def solution():
    num_days = 7
    recommended_sleep = 8
    actual_sleep_days = 2
    actual_sleep_hours = 3
    partial_sleep_days = num_days - actual_sleep_days

    # Calculate the total hours of actual sleep
    actual_sleep = (actual_sleep_days * actual_sleep_hours) + (partial_sleep_days * recommended_sleep * 0.6)
    result = actual_sleep
    return result

print(solution())