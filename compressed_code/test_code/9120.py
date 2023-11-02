def solution():
    
    daily_allowance = 12
    days_in_week = 7
    savings = 0
    for day in range(1, days_in_week+1):
        if day == 4: 
            savings += daily_allowance * 0.25
        else:
            savings += daily_allowance * 0.5
    result = savings
    return result

print(solution())