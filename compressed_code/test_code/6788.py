def solution():
    
    daily_pay = 80
    total_days = 20
    total_spent = 1360
    total_earned = daily_pay * total_days
    amount_saved = total_earned - total_spent
    result = amount_saved
    return result

print(solution())