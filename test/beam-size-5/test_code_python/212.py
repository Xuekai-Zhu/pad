def solution():
    
    borrowed_balance = 2000
    promised_balance = borrowed_balance * 0.1
    monthly_payment = 165
    remaining_balance = borrowed_balance + promised_balance - monthly_payment
    result = remaining_balance
    return result

print(solution())