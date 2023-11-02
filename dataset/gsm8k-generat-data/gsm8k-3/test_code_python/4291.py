def solution():
    """Lizzy had $30. She loaned out $15 to her friend. How much will Lizzy have if her friend returned the money with an interest of 20%?"""
    # Define the initial amount Lizzy had and the amount loaned out
    initial_amount = 30
    loaned_amount = 15

    # Calculate the interest earned on the loaned amount
    interest = loaned_amount * 0.2

    # Calculate the total amount Lizzy will have after her friend returns the money with interest
    total_amount = initial_amount + loaned_amount + interest

    # Display the total amount Lizzy will have
    result = total_amount
    return result

print(solution())