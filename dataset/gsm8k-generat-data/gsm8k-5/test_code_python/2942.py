def solution():
    monthly_payment = 150.00  # Gunther's monthly payment is $150.00
    num_of_months = 5 * 12  # Gunther is financing the tractor for 5 years, or 60 months

    # Calculate the total amount financed by Gunther
    total_finance = monthly_payment * num_of_months
    result = total_finance
    return result

print(solution())