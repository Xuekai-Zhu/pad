def solution():
    
    borrowed_amount = 300
    additional_amount = borrowed_amount * 0.02
    total_amount = borrowed_amount + additional_amount
    monthly_payment = 25
    remaining_amount = total_amount - monthly_payment
    twelfth_month_payment = remaining_amount / 2
    result = twelfth_month_payment
    return result

print(solution())