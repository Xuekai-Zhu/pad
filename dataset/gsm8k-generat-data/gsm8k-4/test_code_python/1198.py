def solution():
    """Arthur has $200 in his wallet. He spends four-fifths of that. How much does he have left?"""
    # Define the initial amount in Arthur's wallet
    initial_amount = 200

    # Calculate the amount spent by Arthur
    amount_spent = initial_amount * (4/5)

    # Calculate the amount remaining in Arthur's wallet
    remaining_amount = initial_amount - amount_spent

    # Return the remaining amount
    result = remaining_amount
    return result

print(solution())