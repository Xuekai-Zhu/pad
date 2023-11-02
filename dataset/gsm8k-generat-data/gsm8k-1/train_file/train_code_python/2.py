def solution():
    """Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?"""
    wallet_cost = 100
    current_savings = wallet_cost / 2
    parents_money = 15
    grandparents_money = parents_money * 2
    total_money = current_savings + parents_money + grandparents_money
    money_needed = wallet_cost - total_money
    result = money_needed
    return result

print(solution())