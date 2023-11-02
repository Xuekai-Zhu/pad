def solution():
    additional_percent = 10/100  # Yoque promised to pay an additional 10% of the borrowed money
    additional_months = 1  # Yoque has to pay back the borrowed money in 11 months
    monthly_payment = 15  # Yoque pays $15 per month

    # Calculate the total amount paid back in 11 months
    total_paid_back = (11 * monthly_payment)

    # Calculate the original borrowed amount
    borrowed_amount = total_paid_back / (1 + additional_percent + additional_months)
    result = borrowed_amount
    return result

print(solution())