def solution():
    """Angus has $20 worth of tokens less than Elsa has. If Elsa has 60 tokens and each token is worth $4, how many tokens does Angus have?"""
    # Define Elsa's total worth of tokens and the value of each token
    elsa_total = 60 * 4
    
    # Define Angus's total as $20 less than Elsa's
    angus_total = elsa_total - 20
    
    # Calculate Angus's total number of tokens
    angus_tokens = angus_total / 4
    
    result = angus_tokens
    return result

print(solution())