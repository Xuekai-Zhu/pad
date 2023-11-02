def solution():
    """Diane is playing poker with her friends and is not having very good luck. She starts with $100 and wins 5 hands for a total of $65 dollars to add to her $100. Emboldened, she begins betting bigger and riskier and ends up losing all her money and owing her friends $50. How much money did Diane lose in all?"""
    # Define the initial amount of money Diane has
    initial_amount = 100

    # Define the amount of money Diane wins
    win_amount = 65

    # Define the amount of money Diane owes
    debt_amount = 50

    # Calculate the total amount of money Diane had
    total_amount = initial_amount + win_amount

    # Calculate the amount of money Diane lost
    loss_amount = total_amount + debt_amount

    # Display the total amount of money Diane lost
    result = loss_amount
    return result

print(solution())