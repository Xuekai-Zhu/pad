def solution():
    """Samantha sleeps an average of 8 hours a night. Her baby sister sleeps 2.5 times as much as Samantha does. Because her father is so tired from watching the baby, for every hour the baby sleeps, he sleeps 30 minutes. How many hours does her father sleep in a week?"""
    samantha_sleep = 8
    baby_sleep = 2.5 * samantha_sleep
    father_sleep = 0.5 * baby_sleep
    hours_per_day = samantha_sleep + baby_sleep + father_sleep
    hours_per_week = hours_per_day * 7
    result = hours_per_week
    return result

print(solution())