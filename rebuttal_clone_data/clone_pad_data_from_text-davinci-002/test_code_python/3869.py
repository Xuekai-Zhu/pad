def solution():
    ideal_nightly_sleep = 8
    actual_sleep_weekdays = 5
    actual_sleep_weekends = 6
    sleep_deficit_weekdays = ideal_nightly_sleep - actual_sleep_weekdays
    sleep_deficit_weekends = actual_sleep_weekends - ideal_nightly_sleep
    sleep_deficit_total = sleep_deficit_weekdays + sleep_deficit_weekends
    return sleep_deficit_total

print(solution())