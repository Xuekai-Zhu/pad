def solution():
    
    laptop_cost = 1000
    down_payment_percentage = 20
    down_payment = laptop_cost * (down_payment_percentage / 100) + 20
    balance = laptop_cost - down_payment
    monthly_payment = 65
    total_payment_after_4_months = monthly_payment * 4
    remaining_balance = balance - total_payment_after_4_months
    result = remaining_balance
    return result

print(solution())