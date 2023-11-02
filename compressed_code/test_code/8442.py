def solution():
    
    total_price = 18000
    deposit = 3000
    remaining_price = total_price - deposit
    num_installments = 6
    monthly_payment = remaining_price / num_installments
    result = monthly_payment
    return result

print(solution())