def solution():
    elsa_tokens = 60  # Elsa has 60 tokens
    token_value = 4  # Each token is worth $4
    angus_tokens_value = elsa_tokens * token_value - 20  # Angus has $20 worth of tokens less than Elsa
    angus_tokens = angus_tokens_value / token_value  # Calculate the number of tokens Angus has
    result = angus_tokens
    return result

print(solution())