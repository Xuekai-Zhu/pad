def solution():
    total_price = 13380
    paid_upfront = 5400
    monthly_payment = 420

    # Calculate the remaining balance
    remaining_balance = total_price - paid_upfront

    # Calculate the number of months needed to fully pay off the remaining balance
    num_months = remaining_balance / monthly_payment
    result = num_months
    return result

print(solution())