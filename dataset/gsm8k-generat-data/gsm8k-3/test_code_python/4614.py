def solution():
    """Yasmin deposited a $50 birthday check from her grandmother in her bank account. The check was worth a quarter of her new balance after the check money is added. How many dollars were in her account before she deposited the check?"""
    # Define the amount of the birthday check
    check_amount = 50

    # Let x be the original balance before the check was deposited
    # After depositing the check, the new balance is x + 50
    # The check was worth 1/4 of the new balance, so we have:
    # check_amount = (x + 50) / 4

    # Solving for x, we get:
    x = (check_amount * 4) - 50

    # Display the original balance
    result = x
    return result

print(solution())