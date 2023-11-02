def solution():
    # Define the value of each token
    token_value = 4
    
    # Calculate Elsa's total token value
    elsa_token_value = 60 * token_value
    
    # Calculate Angus's total token value
    angus_token_value = elsa_token_value - 20
    
    # Calculate Angus's number of tokens
    angus_tokens = angus_token_value / token_value
    result = angus_tokens
    return result

print(solution())