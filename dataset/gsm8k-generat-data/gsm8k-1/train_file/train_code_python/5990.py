def solution():
    """Megan’s grandma gave her $125 to start a savings account. She was able to increase the account by 25% from funds she earned babysitting. Then it decreased by 20% when she bought a new pair of shoes. Her final balance is what percentage of her starting balance?"""
    starting_balance = 125
    increase_percent = 25
    increase_amount = starting_balance * (increase_percent / 100)
    balance_after_increase = starting_balance + increase_amount
    decrease_percent = 20
    decrease_amount = balance_after_increase * (decrease_percent / 100)
    final_balance = balance_after_increase - decrease_amount
    percent_of_starting_balance = (final_balance / starting_balance) * 100
    result = percent_of_starting_balance
    return result

print(solution())