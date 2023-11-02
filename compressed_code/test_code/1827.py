def solution():
    
    monthly_rate = 50
    discount_rate = 0.05
    discount_amount = monthly_rate * discount_rate
    total_amount_per_month = monthly_rate - discount_amount
    total_amount_paid = total_amount_per_month * 4
    result = total_amount_paid
    return result

print(solution())