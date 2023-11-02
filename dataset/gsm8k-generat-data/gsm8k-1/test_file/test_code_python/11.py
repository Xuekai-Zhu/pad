def solution():
    """A merchant wants to make a choice of purchase between 2 purchase plans: jewelry worth $5,000 or electronic gadgets worth $8,000.
    His financial advisor speculates that the jewelry market will go up 2.5% while the electronic gadgets market will rise 1.2% within the same month.
    If the merchant is looking to maximize profit at the end of this month by making a choice, how much profit would this be?"""
    
    jewelry_cost = 5000
    electronic_cost = 8000
    
    jewerly_profit = jewelry_cost * 0.025
    electronic_profit = electronic_cost * 0.012
    
    if jewerly_profit > electronic_profit:
        profit = jewerly_profit
    else:
        profit = electronic_profit
    
    return profit

print(solution())