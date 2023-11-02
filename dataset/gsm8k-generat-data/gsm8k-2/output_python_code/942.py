def solution():
    """Javier is selling donuts to raise money for a new game. He wants to raise $96. He buys each dozen donuts for $2.40 and then sells each donut for $1. How many dozen donuts does he need to buy and sell to reach his goal?"""
    total_profit = 96
    cost_per_dozen = 2.4
    revenue_per_donut = 1
    donuts_per_dozen = 12
    
    # calculate profit per dozen donuts
    profit_per_dozen = (revenue_per_donut * donuts_per_dozen) - cost_per_dozen
    
    # calculate how many dozen donuts are needed to reach the goal
    dozens_needed = total_profit / profit_per_dozen
    
    result = dozens_needed
    return result

print(solution())