def solution():
    """Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?"""
    wallet_price = 100
    current_savings = wallet_price / 2
    parents_help = 15
    grandparents_help = 2 * parents_help
    total_money = current_savings + parents_help + grandparents_help
    needed_money = wallet_price - total_money
    result = needed_money
    return result

print(solution())