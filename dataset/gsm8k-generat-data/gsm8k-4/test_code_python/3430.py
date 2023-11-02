def solution():
    """Samantha sleeps an average of 8 hours a night. Her baby sister sleeps 2.5 times as much as Samantha does. Because her father is so tired from watching the baby, for every hour the baby sleeps, he sleeps 30 minutes. How many hours does her father sleep in a week?"""
    # Calculate Samantha's average sleep time in a week
    samantha_sleep = 8 * 7

    # Calculate the baby's sleep time in a week
    baby_sleep = samantha_sleep * 2.5

    # Calculate the father's sleep time in a week
    father_sleep = baby_sleep * 0.5

    # Return the result
    result = father_sleep / 60
    return result

print(solution())