def solution():
    # Define the cost of the wallet
    wallet_cost = 100

    # Calculate how much money Betty has saved
    betty_savings = wallet_cost / 2

    # Calculate how much money Betty's parents and grandparents give her
    parents_money = 15
    grandparents_money = parents_money * 2

    # Calculate the total amount of money Betty has
    total_money = betty_savings + parents_money + grandparents_money

    # Calculate how much more money Betty needs
    money_needed = wallet_cost - total_money
    result = money_needed
    return result

print(solution())