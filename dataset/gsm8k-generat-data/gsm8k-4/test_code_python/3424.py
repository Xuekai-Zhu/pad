def solution():
    """Larry spent $5 for lunch and gave his brother $2. How much did Larry have at the beginning if he has $15 now?"""
    # Define the amount Larry has now and the amount he spent/gave away
    current_amount = 15
    spent_amount = 5 + 2

    # Calculate the initial amount Larry had
    initial_amount = current_amount + spent_amount

    result = initial_amount
    return result

print(solution())