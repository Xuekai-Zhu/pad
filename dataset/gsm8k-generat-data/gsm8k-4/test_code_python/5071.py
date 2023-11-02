def solution():
    """A football club has a balance of $100 million. The club then sells 2 of its players at $10 million each, and buys 4 more at $15 million each. How much money is left in the club register in millions of dollars?"""
    # Define the initial balance
    balance = 100

    # Sell 2 players at $10 million each
    balance += 2 * 10

    # Buy 4 players at $15 million each
    balance -= 4 * 15

    # Convert to million dollars and round to 2 decimal places
    result = round(balance, 2)
    return result

print(solution())