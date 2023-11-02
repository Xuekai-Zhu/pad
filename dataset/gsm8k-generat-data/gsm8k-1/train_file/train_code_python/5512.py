def solution():
    """An investor invested some money in 2 separate schemes: A and B. Scheme A will yield 30% of the capital within a year, and scheme B will yield 50% of the capital within a year. If he invested $300 in scheme A and $200 in B, how much more money will he have in scheme A than in B after a year, provided he does not withdraw anything?"""
    investment_A = 300
    investment_B = 200
    interest_rate_A = 30
    interest_rate_B = 50
    
    # Calculate the total amount after a year for each scheme 
    amount_A = investment_A + (investment_A * (interest_rate_A / 100))
    amount_B = investment_B + (investment_B * (interest_rate_B / 100))
    
    # Calculate the difference in the amounts
    difference = amount_A - amount_B
    result = difference
    return result

print(solution())