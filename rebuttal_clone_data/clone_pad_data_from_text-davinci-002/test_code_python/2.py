def solution():
     """Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?"""
    wallet_cost = 100
     half_wallet_cost = wallet_cost / 2
     parents_gift = 15
     grandparents_gift = parents_gift * 2
     total_gift = parents_gift + grandparents_gift
     money_needed = half_wallet_cost - total_gift
     result = money_needed
     return result

print(solution())