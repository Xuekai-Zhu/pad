def solution():
    
    credit_limit = 100
    paid_on_tuesday = 15
    paid_on_thursday = 23
    remaining_balance = credit_limit - paid_on_tuesday - paid_on_thursday
    result = remaining_balance
    return result

print(solution())