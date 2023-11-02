def solution():
    """MegaCorp got caught leaking carcinogens into the water supply and is being fined 1% of its annual profits. 
    Every day MegaCorp earns $3,000,000 from mining and $5,000,000 from oil refining. 
    Its monthly expenses are $30,000,000. How much is MegaCorp's fine in dollars?"""
    
    # Calculate MegaCorp's daily earnings
    daily_earnings = (3_000_000 * 30) + (5_000_000 * 30)
    
    # Calculate MegaCorp's monthly earnings
    monthly_earnings = daily_earnings * 30
    
    # Calculate MegaCorp's annual earnings
    annual_earnings = monthly_earnings * 12
    
    # Calculate MegaCorp's annual profit by subtracting expenses from earnings
    annual_profit = annual_earnings - (30_000_000 * 12)
    
    # Calculate MegaCorp's fine
    fine = annual_profit * 0.01
    
    result = fine
    return result

print(solution())