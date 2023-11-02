def solution():
    """A football club has a balance of $100 million. The club then sells 2 of its players at $10 million each, and buys 4 more at $15 million each. How much money is left in the club register in millions of dollars?"""

    # Define the initial balance of the club
    initial_balance = 100

    # Calculate the amount earned from selling the 2 players
    earnings = 2 * 10

    # Calculate the amount spent on buying 4 new players
    expenses = 4 * 15

    # Calculate the new balance of the club
    new_balance = initial_balance + earnings - expenses

    # Display the new balance
    result = new_balance
    return result

print(solution())