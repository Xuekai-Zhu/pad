def solution():
    cash_price = 450
    down_payment = 100
    month1_to_4 = 40
    month5_to_8 = 35
    month9_to_12 = 30

    # Calculate the total installment payments
    total_installment_payments = down_payment + (month1_to_4 * 4) + (month5_to_8 * 4) + (month9_to_12 * 4)

    # Calculate the total amount saved by buying in cash
    total_savings = cash_price - total_installment_payments
    result = total_savings
    return result

print(solution())