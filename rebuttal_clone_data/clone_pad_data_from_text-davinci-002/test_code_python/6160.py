def solution():
    cash_price = 8000
    deposit = 3000
    monthly_payment = 300
    total_payments = monthly_payment * 30
    total_saved = cash_price - (deposit + total_payments)
    result = total_saved
    return result

print(solution())