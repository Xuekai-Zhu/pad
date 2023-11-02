def solution():
    """Megan’s grandma gave her $125 to start a savings account. She was able to increase the account by 25% from funds she earned babysitting. Then it decreased by 20% when she bought a new pair of shoes. Her final balance is what percentage of her starting balance?"""
    # Define the starting balance
    starting_balance = 125

    # Calculate the balance after increasing it by 25%
    increase = starting_balance * 0.25
    new_balance = starting_balance + increase

    # Calculate the balance after decreasing it by 20%
    decrease = new_balance * 0.2
    final_balance = new_balance - decrease

    # Calculate the percentage of the final balance compared to the starting balance
    percentage = (final_balance / starting_balance) * 100

    # Return the result
    result = percentage
    return result

print(solution())