def solution():
    """John goes to the store to buy Slurpees and gives them $20.  Slurpees cost $2 each and he got $8 in change.  How many Slurpees did he buy?"""
    # Define the cost of one Slurpee and the amount of money John gave
    SLURPEE_COST = 2
    MONEY_GIVEN = 20

    # Calculate how much money John spent on Slurpees
    money_spent = MONEY_GIVEN - 8
    slurpee_count = money_spent // SLURPEE_COST

    # Display the number of Slurpees John bought
    result = slurpee_count
    return result

print(solution())