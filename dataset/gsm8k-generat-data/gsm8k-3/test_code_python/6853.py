def solution():
    """Isabelle’s parents bought a new television for $480. The seller gives them a 5% discount. They pay a first installment of $150 and will pay the rest in 3 monthly installments. What is the amount of a monthly payment?"""
    # Define the original price and discount rate
    ORIGINAL_PRICE = 480
    DISCOUNT_RATE = 0.05

    # Calculate the discounted price
    discounted_price = ORIGINAL_PRICE * (1 - DISCOUNT_RATE)

    # Calculate the remaining balance after the first installment
    remaining_balance = discounted_price - 150

    # Calculate the monthly payment amount
    monthly_payment = remaining_balance / 3

    # Display the monthly payment amount
    result = monthly_payment
    return result

print(solution())