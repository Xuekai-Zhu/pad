def solution():
    """Angus has $20 worth of tokens less than Elsa has. If Elsa has 60 tokens and each token is worth $4, how many tokens does Angus have?"""
    # Define the value of each token in dollars
    TOKEN_VALUE = 4

    # Calculate the value of Elsa's tokens
    elsa_value = 60 * TOKEN_VALUE

    # Calculate Angus's value of tokens
    angus_value = elsa_value - 20

    # Calculate the number of tokens Angus has
    angus_tokens = angus_value / TOKEN_VALUE

    # Display the number of tokens Angus has
    result = angus_tokens
    return result

print(solution())