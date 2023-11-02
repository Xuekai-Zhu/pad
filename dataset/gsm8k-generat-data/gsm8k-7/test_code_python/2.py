def solution():
    wallet_cost = 100
    betty_saved = wallet_cost / 2
    parents_contribution = 15
    grandparents_contribution = parents_contribution * 2

    # Calculate the total amount of money Betty has for the wallet
    total_money = betty_saved + parents_contribution + grandparents_contribution

    # Calculate the amount of money Betty still needs to buy the wallet
    remaining_cost = wallet_cost - total_money

    result = remaining_cost
    return result

print(solution())