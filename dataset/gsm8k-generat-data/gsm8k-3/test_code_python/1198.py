def solution():
    """Arthur has $200 in his wallet. He spends four-fifths of that. How much does he have left?"""
    # Define Arthur's initial balance
    initial_balance = 200

    # Calculate how much Arthur spends
    amount_spent = 4 / 5 * initial_balance

    # Calculate Arthur's remaining balance
    remaining_balance = initial_balance - amount_spent

    # Display Arthur's remaining balance
    result = remaining_balance
    return result

print(solution())