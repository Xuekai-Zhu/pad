def solution():
    """Javier is selling donuts to raise money for a new game. He wants to raise $96. He buys each dozen donuts for $2.40 and then sells each donut for $1. How many dozen donuts does he need to buy and sell to reach his goal?"""
    goal_amount = 96
    cost_per_dozen = 2.4
    sell_price_per_donut = 1
    donuts_per_dozen = 12
    
    # Determine profit per dozen donuts
    profit_per_dozen = sell_price_per_donut * donuts_per_dozen - cost_per_dozen
    
    # Determine number of dozen donuts needed to reach goal
    dozens_needed = int(goal_amount / profit_per_dozen)
    if goal_amount % profit_per_dozen != 0:
        dozens_needed += 1
    
    result = dozens_needed
    return result

print(solution())