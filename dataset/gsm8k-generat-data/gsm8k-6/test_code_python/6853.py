def solution():
    # Calculate the total amount paid after the discount
    total = 480 * 0.95  # 5% discount applied to $480

    # Calculate the remaining amount to be paid
    remaining = total - 150  # first installment already paid

    # Calculate the monthly payment value
    monthly_payment = remaining / 3  # remaining amount divided into 3 monthly installments

    result = monthly_payment
    return result

print(solution())