def solution():
    # Calculate the discounted price of the TV
    discounted_price = 0.95 * 480
    
    # Calculate the remaining balance after the first installment
    remaining_balance = discounted_price - 150
    
    # Calculate the monthly payment
    monthly_payment = remaining_balance / 3
    
    result = monthly_payment
    return result

print(solution())