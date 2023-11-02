def solution():
    """Jane is trying to decide whether to buy a house or a trailer. A house costs $480,000 and a trailer costs $120,000. Each loan will be paid in monthly installments over 20 years. How much more is the monthly payment on the house compared to the trailer?"""
    # Define the cost of the house and trailer
    HOUSE_COST = 480000
    TRAILER_COST = 120000

    # Define the number of monthly payments and the interest rate
    NUM_PAYMENTS = 20 * 12
    INTEREST_RATE = 0.05 / 12

    # Calculate the monthly payment for the house
    house_payment = (HOUSE_COST * INTEREST_RATE) / (1 - (1 + INTEREST_RATE) ** (-NUM_PAYMENTS))

    # Calculate the monthly payment for the trailer
    trailer_payment = (TRAILER_COST * INTEREST_RATE) / (1 - (1 + INTEREST_RATE) ** (-NUM_PAYMENTS))

    # Calculate the difference in monthly payments between the house and trailer
    monthly_difference = house_payment - trailer_payment

    # Display the monthly difference
    result = monthly_difference
    return result

print(solution())