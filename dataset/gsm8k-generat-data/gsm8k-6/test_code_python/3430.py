def solution():
    samantha_sleep = 8  # hours slept by Samantha per night
    baby_sleep = 2.5 * samantha_sleep  # hours slept by baby sister per night
    father_sleep = 0.5 * baby_sleep  # hours father sleeps for each hour baby sister sleeps
    total_sleep = 7 * (samantha_sleep + baby_sleep) + 7 * 24 * father_sleep  # total hours slept in a week
    result = total_sleep / 24  # convert to days
    return result

print(solution())