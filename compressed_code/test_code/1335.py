def solution():
    
    original_balance = 150.00
    payment = 50.00
    remaining_balance = original_balance - payment
    if remaining_balance > 0:
        new_balance = remaining_balance * 1.2
    else:
        new_balance = 0
    result = new_balance
    return result

print(solution())