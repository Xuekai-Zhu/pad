def solution():
    samantha_sleeps = 8
    baby_sleeps = 2.5 * samantha_sleeps
    father_sleep_ratio = 0.5  # Father sleeps half as much as the baby

    hours_per_day = samantha_sleeps + baby_sleeps
    hours_per_week = hours_per_day * 7

    father_sleep_hours = father_sleep_ratio * baby_sleeps * 7

    total_sleep_hours = hours_per_week + father_sleep_hours
    result = total_sleep_hours
    return result

print(solution())