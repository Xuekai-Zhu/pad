def solution():
    balance = 150
    payment = 50
    interest = 20
    
    new_balance = balance - payment
    new_balance_with_interest = new_balance + (new_balance * (interest / 100))
    
    result = new_balance_with_interest
    
    return result

print(solution())