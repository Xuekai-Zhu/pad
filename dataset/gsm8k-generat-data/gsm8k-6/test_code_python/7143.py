def solution():
    # Calculate the value of the tokens that Elsa has
    elsa_tokens_value = 60 * 4  # each token is worth $4

    # Calculate the value of the tokens that Angus has
    angus_tokens_value = elsa_tokens_value - 20  # Angus has $20 less than Elsa

    # Calculate the number of tokens that Angus has
    angus_tokens = angus_tokens_value / 4  # each token is worth $4

    result = angus_tokens
    return result

print(solution())