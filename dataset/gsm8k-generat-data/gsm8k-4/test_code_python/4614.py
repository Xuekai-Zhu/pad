def solution():
    """Yasmin deposited a $50 birthday check from her grandmother in her bank account. The check was worth a quarter of her new balance after the check money is added. How many dollars were in her account before she deposited the check?"""
    # Define the initial balance
    initial_balance = None

    # Define the check amount
    check_amount = 50

    # Define the fraction of the new balance represented by the check
    check_fraction = 0.25

    # Calculate the equation for the new balance after the check is added
    # new balance = old balance + check amount = 1.25 * old balance
    # Therefore: old balance = new balance / 1.25
    new_balance = check_amount / check_fraction
    initial_balance = new_balance / 1.25

    result = initial_balance
    return result

print(solution())