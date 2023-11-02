def solution():
    """Jeff orders a Halloween costume. He has to put in a 10% deposit and then pay the rest when he picks it up. The costume is 40% more expensive than last year's costume, which cost $250. How much did he pay when picking it up, in dollars?"""
    # Define the cost of last year's costume and the deposit percentage
    last_year_costume = 250
    deposit_percentage = 0.1

    # Calculate the cost of the deposit
    deposit = last_year_costume * deposit_percentage

    # Calculate the total cost of this year's costume
    this_year_costume = last_year_costume * 1.4

    # Subtract the deposit from the total cost to get the final payment amount
    final_payment = this_year_costume - deposit

    # Return the result
    result = final_payment
    return result

print(solution())