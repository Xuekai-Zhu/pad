def solution():
    """An investor invested some money in 2 separate schemes: A and B. Scheme A will yield 30% of the capital within a year, and scheme 
    B will yield 50% of the capital within a year. If he invested $300 in scheme A and $200 in B, how much more money will he have in 
    scheme A than in B after a year, provided he does not withdraw anything?"""
    # Define the initial investments
    investment_a = 300
    investment_b = 200
    
    # Calculate the returns after a year
    returns_a = investment_a * 1.3
    returns_b = investment_b * 1.5
    
    # Calculate the difference in returns
    difference = returns_a - returns_b
    
    # return the result
    result = difference
    return result

print(solution())