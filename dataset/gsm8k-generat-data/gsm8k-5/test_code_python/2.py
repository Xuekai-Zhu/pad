def solution():
    cost_of_wallet = 100  # The cost of the wallet Betty wants to buy
    money_saved = 0.5 * cost_of_wallet  # Betty has saved half of the money she needs
    parents_money = 15  # Betty's parents give her $15
    grandparents_money = 2 * parents_money  # Betty's grandparents give her twice as much as her parents

    # Calculate the total amount of money Betty has for the wallet
    total_money = money_saved + parents_money + grandparents_money

    # Calculate the remaining amount Betty needs to buy the wallet
    remaining_money = cost_of_wallet - total_money
    result = remaining_money
    return result

print(solution())