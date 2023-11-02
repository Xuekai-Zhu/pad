def solution():
    """Samantha sleeps an average of 8 hours a night. Her baby sister sleeps 2.5 times as much as Samantha does. Because her father is so tired from watching the baby, for every hour the baby sleeps, he sleeps 30 minutes. How many hours does her father sleep in a week?"""
    samantha_sleeps = 8
    baby_sleeps = 2.5 * samantha_sleeps
    father_sleeps_per_baby_hour = 0.5
    father_sleeps_per_day = father_sleeps_per_baby_hour * baby_sleeps
    father_sleeps_per_week = father_sleeps_per_day * 7
    result = father_sleeps_per_week
    return result

print(solution())