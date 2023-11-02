def solution():
    """There were 21 dollars in the cookie jar. Doris spent $6 from the cookie jar. Martha spent half as much as Doris. How much money, in dollars, was left in the cookie jar?"""
    # Define the initial amount of money in the cookie jar
    initial_amount = 21

    # Doris spent $6 from the cookie jar
    doris_spent = 6

    # Martha spent half as much as Doris
    martha_spent = doris_spent / 2

    # Calculate the total amount spent
    total_spent = doris_spent + martha_spent

    # Calculate the amount of money left in the cookie jar
    amount_left = initial_amount - total_spent

    # return the result
    result = amount_left
    return result

print(solution())