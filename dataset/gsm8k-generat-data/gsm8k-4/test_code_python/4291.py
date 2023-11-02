def solution():
    """Lizzy had $30. She loaned out $15 to her friend. How much will Lizzy have if her friend returned the money with an interest of 20%?"""
    # Define the initial amount Lizzy had and the amount she loaned out
    initial_amount = 30
    loaned_amount = 15

    # Define the interest rate and calculate the interest
    interest_rate = 0.2
    interest = loaned_amount * interest_rate

    # Add the interest to the loaned amount to get the total amount to be returned
    total_returned = loaned_amount + interest

    # Add the total returned amount to Lizzy's initial amount
    final_amount = initial_amount + total_returned

    # Return the final amount
    result = final_amount
    return result

print(solution())