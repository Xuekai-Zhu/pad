def solution():
    
    cash_price = 400
    down_payment = 120
    monthly_payment = 30
    months = 12
    total_price = down_payment + (monthly_payment * months)
    savings = total_price - cash_price
    result = savings
    return result

print(solution())