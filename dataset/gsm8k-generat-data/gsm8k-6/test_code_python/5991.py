def solution():
    starting_balance = 125  # grandma gave Megan $125 to start a savings account
    increased_balance = starting_balance * 1.25  # Megan increased her account by 25%
    decreased_balance = increased_balance * 0.8  # Megan’s balance decreased by 20% after buying shoes
    final_balance_percent = (decreased_balance / starting_balance) * 100  # final balance as a percentage of starting balance
    result = final_balance_percent
    return result

print(solution())