def solution():
    """Gunther just financed a John Deere tractor through the dealership.  If his monthly payment is $150.00 a month, for 5 years, with no interest, how much did he finance the tractor for?"""
    # Define the length of the loan and the monthly payment
    loan_length = 5 * 12  # 5 years converted to months
    monthly_payment = 150

    # Calculate the total amount paid over the life of the loan
    total_paid = loan_length * monthly_payment

    # Calculate the original amount financed
    original_amount = total_paid

    # Return the result
    result = original_amount
    return result

print(solution())