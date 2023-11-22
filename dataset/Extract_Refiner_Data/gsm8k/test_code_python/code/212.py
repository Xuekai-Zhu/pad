def solution():
    
    borrowed_amount = 2000
    promised_amount = borrowed_amount * 0.1
    total_amount = borrowed_amount + promised_amount
    monthly_payment = 165
    months = 12
    remaining_balance = total_amount - monthly_payment * months
    result = remaining_balance
    return result

print(solution())