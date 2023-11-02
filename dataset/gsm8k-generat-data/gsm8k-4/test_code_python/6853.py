def solution():
    """Isabelle’s parents bought a new television for $480. The seller gives them a 5% discount. They pay a first installment of $150 and will pay the rest in 3 monthly installments. What is the amount of a monthly payment?"""
    # Define the initial price of the television and the discount percentage
    initial_price = 480
    discount_percentage = 0.05

    # Calculate the amount of the discount
    discount_amount = initial_price * discount_percentage

    # Calculate the discounted price
    discounted_price = initial_price - discount_amount

    # Calculate the amount remaining to be paid
    remaining_amount = discounted_price - 150

    # Calculate the amount of each monthly payment
    monthly_payment = remaining_amount / 3

    # return the result
    result = monthly_payment
    return result

print(solution())