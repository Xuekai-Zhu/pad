def solution():
    """Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?"""
    # Define the cost of the wallet and the current amount of money Betty has
    wallet_cost = 100
    current_money = wallet_cost / 2

    # Define the amount of money given by her parents and grandparents
    parents_money = 15
    grandparents_money = 2 * parents_money

    # Calculate the total amount of money Betty has now
    total_money = current_money + parents_money + grandparents_money

    # Calculate the amount of money still needed to buy the wallet
    still_needed = wallet_cost - total_money

    result = still_needed
    return result

print(solution())