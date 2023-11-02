def solution():
    """Megan’s grandma gave her $125 to start a savings account. She was able to increase the account by 25% from funds she earned babysitting. Then it decreased by 20% when she bought a new pair of shoes. Her final balance is what percentage of her starting balance?"""
    # Define Megan's starting balance and the percentage increase and decrease
    starting_balance = 125
    increase_percentage = 25
    decrease_percentage = 20

    # Calculate Megan's balance after the increase
    balance_after_increase = starting_balance + (starting_balance * (increase_percentage / 100))

    # Calculate Megan's balance after the decrease
    balance_after_decrease = balance_after_increase - (balance_after_increase * (decrease_percentage / 100))

    # Calculate Megan's final balance as a percentage of her starting balance
    final_balance_percentage = (balance_after_decrease / starting_balance) * 100

    # Display Megan's final balance as a percentage of her starting balance
    result = final_balance_percentage
    return result

print(solution())