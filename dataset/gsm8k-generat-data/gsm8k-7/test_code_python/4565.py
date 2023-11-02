def solution():
    num_months = 11
    total_interest = 0.10
    monthly_payment = 15

    # Calculate the total amount of money paid by Yoque over the 11 months
    total_paid = num_months * monthly_payment

    # Calculate the original amount borrowed by Yoque
    original_amount = total_paid / (1 + total_interest)
    result = original_amount
    return result

print(solution())