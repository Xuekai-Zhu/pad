def solution():
    
    balance = 150
    payment = 50
    interest_rate = 0.2
    balance_after_payment = balance - payment
    new_balance = balance_after_payment + (balance_after_payment * interest_rate)
    result = new_balance
    return result

print(solution())