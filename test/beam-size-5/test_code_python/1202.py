def solution():
    # Calculate the loan amount
    loan_amount = 250000 * 0.4

    # Calculate the amount used to pay off his debt
    debt_amount = loan_amount * 0.6

    # Calculate the amount leftover after paying debt
    leftover_amount = loan_amount - debt_amount
    result = leftover_amount
    return result

print(solution())