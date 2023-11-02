def solution():
    last_month_payment = 15
    total_debt = 50

    # Calculate the total amount Jerry paid in the past two months
    past_payments = 12 + last_month_payment

    # Calculate how much Jerry still owes
    remaining_debt = total_debt - past_payments
    result = remaining_debt
    return result

print(solution())