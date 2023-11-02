def solution():
    """Shawna has 7 acorns. Sheila has 5 times as many acorns as Shawna, but 3 fewer acorns than Danny. How many acorns do they have altogether?"""
    # Define the number of acorns Shawna has
    shawna_acorns = 7
    
    # Define the number of acorns Sheila has (5 times as many as Shawna, but 3 fewer than Danny)
    sheila_acorns = (shawna_acorns * 5) - 3
    
    # Define the number of acorns Danny has (3 more than Sheila)
    danny_acorns = sheila_acorns + 3
    
    # Calculate the total number of acorns
    total_acorns = shawna_acorns + sheila_acorns + danny_acorns
    
    # return the result
    result = total_acorns
    return result

print(solution())