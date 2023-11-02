def solution():
    
    cash_price = 450
    down_payment = 100
    installment_months = 12
    installment_price = down_payment + (40*4) + (35*4) + (30*4)
    savings = installment_price - cash_price
    result = savings
    return result

print(solution())