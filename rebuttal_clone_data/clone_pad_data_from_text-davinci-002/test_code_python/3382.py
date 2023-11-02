def solution():
    days_worked = 300
    vacation_days_used = 5 + (2 * 5)
    vacation_days_earned = days_worked / 10
    vacation_days_remaining = vacation_days_earned - vacation_days_used
    result = vacation_days_remaining
    return result

print(solution())