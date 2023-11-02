def solution():
    """Jeff orders a Halloween costume.  He has to put in a 10% deposit and then pay the rest when he picks it up.  The costume is 40% more expensive than last year's costume, which cost $250.  How much did he pay when picking it up, in dollars?"""
    # Define the cost of last year's costume and the deposit percentage
    LAST_YEAR_COST = 250
    DEPOSIT_PERCENTAGE = 0.1

    # Calculate the cost of this year's costume
    this_year_cost = LAST_YEAR_COST * 1.4

    # Calculate the deposit amount and the remaining balance
    deposit_amount = this_year_cost * DEPOSIT_PERCENTAGE
    balance = this_year_cost - deposit_amount

    # Display the amount paid when picking up the costume
    result = balance
    return result

print(solution())