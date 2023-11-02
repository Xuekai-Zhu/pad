def solution():
    """Last month, you borrowed $100 from your friend. If you promise to pay her today, how much will you give to your friend if both of you agreed to return the money with a 10% increase?"""
    # Define the amount borrowed and the interest rate
    borrowed_amount = 100
    interest_rate = 0.1

    # Calculate the interest amount
    interest_amount = borrowed_amount * interest_rate

    # Calculate the total amount to be returned
    total_amount = borrowed_amount + interest_amount

    # Return the total amount
    result = total_amount
    return result

print(solution())