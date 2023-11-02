def solution():
    
    worked_days = 300
    vacation_days_earned = worked_days // 10
    march_vacation_days = 5
    september_vacation_days = 2 * 5
    total_vacation_days_taken = march_vacation_days + september_vacation_days
    remaining_vacation_days = vacation_days_earned - total_vacation_days_taken
    result = remaining_vacation_days
    return result

print(solution())