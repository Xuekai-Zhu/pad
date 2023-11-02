def solution():
    
    carol_savings = 60
    carol_saving_rate = 9
    mike_savings = 90
    mike_saving_rate = 3
    weeks = 0
    
    while carol_savings != mike_savings:
        carol_savings += carol_saving_rate
        mike_savings += mike_saving_rate
        weeks += 1
        
    result = weeks
    
    return result

print(solution())