def solution():
    
    jake_weekly_newspapers = 234
    miranda_weekly_newspapers = jake_weekly_newspapers * 2
    weeks_in_month = 4
    jake_monthly_newspapers = jake_weekly_newspapers * weeks_in_month
    miranda_monthly_newspapers = miranda_weekly_newspapers * weeks_in_month
    more_newspapers_delivered = miranda_monthly_newspapers - jake_monthly_newspapers
    result = more_newspapers_delivered
    return result

print(solution())