def solution():
    recommended_sleep = 6 # hours
    current_sleep = 4 # hours
    days_in_week = 7

    # Calculate the difference in sleep per day
    sleep_diff = recommended_sleep - current_sleep

    # Calculate the total amount of sleep lacking in a week
    sleep_lack = sleep_diff * days_in_week

    result = sleep_lack
    return result

print(solution())