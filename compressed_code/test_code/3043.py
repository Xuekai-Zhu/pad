def solution():
    
    period_1 = 4
    period_2 = 2 * period_1
    period_3 = period_2 - 3
    total_shots = 21
    shots_in_period_4 = total_shots - period_1 - period_2 - period_3
    result = shots_in_period_4
    return result

print(solution())