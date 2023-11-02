def solution():
    """Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?"""
    # Define the cost of the wallet and the money Betty has saved
    WALLET_COST = 100
    BETTY_SAVINGS = WALLET_COST / 2

    # Define the money Betty gets from her parents and grandparents
    PARENTS_MONEY = 15
    GRANDPARENTS_MONEY = PARENTS_MONEY * 2

    # Calculate the total money Betty has
    total_money = BETTY_SAVINGS + PARENTS_MONEY + GRANDPARENTS_MONEY

    # Calculate the remaining money Betty needs to buy the wallet
    remaining_money = WALLET_COST - total_money

    # return the result
    result = remaining_money
    return result

print(solution())