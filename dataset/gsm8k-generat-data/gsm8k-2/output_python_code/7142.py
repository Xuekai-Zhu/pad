def solution():
    """Angus has $20 worth of tokens less than Elsa has. If Elsa has 60 tokens and each token is worth $4, how many tokens does Angus have?"""
    elsa_tokens = 60
    token_value = 4
    elsa_value = elsa_tokens * token_value
    angus_value = elsa_value - 20
    angus_tokens = angus_value / token_value
    result = angus_tokens
    return result

print(solution())