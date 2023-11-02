def solution():
    """Angus has $20 worth of tokens less than Elsa has. If Elsa has 60 tokens and each token is worth $4, how many tokens does Angus have?"""
    elsa_tokens = 60
    token_value = 4
    angus_token_value = elsa_tokens * token_value - 20
    angus_tokens = angus_token_value / token_value
    result = angus_tokens
    return result

print(solution())