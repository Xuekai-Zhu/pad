def solution():
    """There were 21 dollars in the cookie jar. Doris spent $6 from the cookie jar. Martha spent half as much as Doris. How much money, in dollars, was left in the cookie jar?"""
    # Define the initial amount in the cookie jar
    initial_amount = 21

    # Calculate the new amount after Doris spends $6
    doris_spending = 6
    amount_after_doris = initial_amount - doris_spending

    # Calculate how much Martha spent
    martha_spending = doris_spending / 2

    # Calculate the final amount in the cookie jar
    final_amount = amount_after_doris - martha_spending

    # Display the final amount in the cookie jar
    result = final_amount
    return result

print(solution())