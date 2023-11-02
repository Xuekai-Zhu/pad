def solution():
    pies_made_per_day = 7
    days_worked = 12
    pies_eaten = 50
    pies_remaining = pies_made_per_day * days_worked - pies_eaten
    result = pies_remaining
    return result

print(solution())