def solution():
    
    pies_per_day = 7
    num_days = 12
    total_pies_made = pies_per_day * num_days
    pies_eaten = 50
    pies_remaining = total_pies_made - pies_eaten
    result = pies_remaining
    return result

print(solution())