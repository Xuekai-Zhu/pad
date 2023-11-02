def solution():
    """Carol has $60 and saves $9 per week. Mike has $90 and saves $3 per week. How many weeks before Carol and Mike both have the same amount of money?"""
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