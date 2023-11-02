def solution():
    
    days_worked = 300
    march_days_off = 5
    september_days_off = 2 * march_days_off
    total_days_off = march_days_off + september_days_off
    vacation_days_earned = days_worked // 10
    vacation_days_taken = total_days_off
    vacation_days_remaining = vacation_days_earned - vacation_days_taken
    result = vacation_days_remaining
    return result

print(solution())