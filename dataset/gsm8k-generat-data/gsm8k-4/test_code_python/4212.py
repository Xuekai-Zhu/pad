def solution():
    """Calculate the total amount of money Braden had in his money box after winning a bet."""
    # Define the initial amount in Braden's money box
    initial_amount = 400

    # Calculate the amount of money Bryan bet on the game
    bryan_bet = initial_amount * 2

    # Assuming the Raptors won, calculate the total amount of money Braden has after winning the bet
    total_amount = initial_amount + bryan_bet * 2

    result = total_amount
    return result

print(solution())