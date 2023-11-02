def solution():
    samantha_sleeps = 8  # hours per night
    baby_sleeps = 2.5 * samantha_sleeps  # baby sister sleeps 2.5 times as much as Samantha
    father_sleeps = 0.5 * baby_sleeps  # for every hour the baby sleeps, father sleeps 30 minutes
    hours_per_week = 7 * (samantha_sleeps + baby_sleeps + father_sleeps)  # 7 days in a week

    result = hours_per_week
    return result

print(solution())