def solution():
    
    daily_allowance = 12
    saved_percent = 0.5
    saved_amount = 0
    for i in range(1, 8):
        if i == 4:
            saved_amount += daily_allowance * 0.25
        else:
            saved_amount += daily_allowance * saved_percent

    result = saved_amount
    return result

print(solution())