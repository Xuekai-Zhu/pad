def solution():
    starting_balance = 125  # Megan's grandma gave her $125 to start a savings account
    increase_percent = 25  # Megan increased the account balance by 25%
    decrease_percent = 20  # Megan decreased the account balance by 20%

    # Calculate the increase in the account balance from babysitting
    increase_amount = (increase_percent / 100) * starting_balance
    new_balance = starting_balance + increase_amount

    # Calculate the decrease in the account balance from buying shoes
    decrease_amount = (decrease_percent / 100) * new_balance
    final_balance = new_balance - decrease_amount

    # Calculate the final balance as a percentage of the starting balance
    percent_of_starting_balance = (final_balance / starting_balance) * 100
    result = percent_of_starting_balance
    return result

print(solution())