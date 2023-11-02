def solution():
    
    daily_recommended = 200
    weekly_recommended = daily_recommended * 7
    pill_dose = 50
    pills_needed = weekly_recommended / pill_dose
    result = pills_needed
    return result

print(solution())