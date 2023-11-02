def solution():
    
    rolls_per_day = 6 * 1
    rolls_per_week = rolls_per_day * 7
    rolls_per_month = rolls_per_week * 4
    rolls_per_dozen = 12
    total_dozen = rolls_per_month / rolls_per_dozen
    result = total_dozen
    return result

print(solution())