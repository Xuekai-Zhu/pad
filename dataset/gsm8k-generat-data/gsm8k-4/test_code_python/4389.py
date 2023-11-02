def solution():
    """Jane is trying to decide whether to buy a house or a trailer. A house costs $480,000 and a trailer costs $120,000. Each loan will be paid in monthly installments over 20 years. How much more is the monthly payment on the house compared to the trailer?"""
    # Define the prices of the house and the trailer and the number of months for the loan
    house_price = 480000
    trailer_price = 120000
    loan_months = 20 * 12

    # Calculate the monthly payment for the house
    house_payment = house_price / loan_months

    # Calculate the monthly payment for the trailer
    trailer_payment = trailer_price / loan_months

    # Calculate the difference in monthly payments
    payment_difference = house_payment - trailer_payment

    # Return the result rounded to 2 decimal places
    result = round(payment_difference, 2)
    return result

print(solution())