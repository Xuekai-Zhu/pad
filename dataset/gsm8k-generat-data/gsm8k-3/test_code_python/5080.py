def solution():
    """Kimmie received $450 from her handmade crafts at the supermarket. Her friend Zahra received 1/3 less money when she sold the same amount of handmade crafts at Etsy. If both of them save half of their earnings on the same savings account, calculate the total amount of money in the joint savings account?"""
    
    #calculate Zahra's earnings
    zahra_earnings = (2/3) * 450
    
    #calculate total earnings
    total_earnings = 450 + zahra_earnings
    
    #calculate the amount saved in the joint savings account
    savings = (1/2) * total_earnings
    
    result = savings
    return result

print(solution())