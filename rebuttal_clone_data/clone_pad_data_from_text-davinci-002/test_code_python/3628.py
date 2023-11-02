def solution():
    extra_chores_per_day = 4
    days_per_week = 7
    weeks = 2
    payment_per_chore = 2
    total_chores = extra_chores_per_day * days_per_week * weeks
    total_earnings = total_chores * payment_per_chore
    result = total_earnings
    return result

print(solution())