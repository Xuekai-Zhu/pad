def solution():
    """Megan's grandma gave her $125 to start a savings account. She was able to increase the account by 25% from funds she earned babysitting.
    Then it decreased by 20% when she bought a new pair of shoes. Her final balance is what percentage of her starting balance?"""
    starting_balance = 125
    increase_percent = 0.25
    decrease_percent = 0.2
    babysitting_earnings = starting_balance * increase_percent
    new_balance = starting_balance + babysitting_earnings
    shoe_cost = new_balance * decrease_percent
    final_balance = new_balance - shoe_cost
    percent_of_starting_balance = (final_balance / starting_balance) * 100
    result = percent_of_starting_balance
    return result

print(solution())