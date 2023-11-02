def solution():
    
    tv_price = 480
    discount = tv_price * 0.05
    discounted_price = tv_price - discount
    remaining_amount = discounted_price - 150
    monthly_installments = 3
    monthly_payment = remaining_amount / monthly_installments
    result = monthly_payment
    return result

print(solution())