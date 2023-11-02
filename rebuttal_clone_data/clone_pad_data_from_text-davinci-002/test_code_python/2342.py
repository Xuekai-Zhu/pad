def solution():
    monthly_rate = 50
    discount_rate = 5
    months_paid = 4
    amount_due = monthly_rate * months_paid
    discount_amount = amount_due * (discount_rate / 100)
    total_paid = amount_due - discount_amount
    result = total_paid
    return result

print(solution())