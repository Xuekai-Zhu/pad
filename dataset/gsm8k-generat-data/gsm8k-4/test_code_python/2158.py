def solution():
    """A housewife goes to the market. She spent 2/3 of her $150. How much does she have left?"""
    # Define the initial amount of money
    initial_amount = 150

    # Calculate the amount spent
    amount_spent = initial_amount * (2/3)

    # Calculate the amount left
    amount_left = initial_amount - amount_spent

    # return the result
    result = amount_left
    return result

print(solution())