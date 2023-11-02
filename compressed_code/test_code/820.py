def solution():
    
    cash_price = 400
    down_payment = 120
    monthly_payment = 30
    total_installment_price = down_payment + (monthly_payment * 12)
    savings = total_installment_price - cash_price
    result = savings
    return result

print(solution())