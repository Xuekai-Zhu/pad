def solution():
    cash_price = 8000
    deposit = 3000
    monthly_installments = 30
    installment_amount = 300

    # Calculate the total amount paid through installments
    total_installment_payment = monthly_installments * installment_amount

    # Calculate the total amount paid by Samantha
    total_paid = deposit + total_installment_payment

    # Calculate the amount she saved by paying in cash
    savings = cash_price - total_paid
    result = savings
    return result

print(solution())