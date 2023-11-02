def solution():
    """MegaCorp got caught leaking carcinogens into the water supply and is being fined 1% of its annual profits. 
    Every day MegaCorp earns $3,000,000 from mining and $5,000,000 from oil refining. Its monthly expenses are $30,000,000. 
    How much is MegaCorp's fine in dollars?"""
    
    daily_profit = 3000000 + 5000000 - 1000000  # subtracting monthly expenses from daily profit
    annual_profit = daily_profit * 365
    fine = annual_profit * 0.01
    result = fine
    
    return result

print(solution())