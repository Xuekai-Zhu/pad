def solution():
    
    weekly_allowance = 20
    extra_chore_pay = 1.5
    total_earnings = 425
    total_weeks = 10
    extra_chore_count = (total_earnings - (weekly_allowance * total_weeks)) / (extra_chore_pay * total_weeks)
    result = extra_chore_count
    return result

print(solution())