def solution():
    elsa_tokens = 60
    token_value = 4

    # Calculate Elsa's total token value
    elsa_total_value = elsa_tokens * token_value

    # Calculate Angus' total token value
    angus_total_value = elsa_total_value - 20

    # Calculate Angus' number of tokens
    angus_tokens = angus_total_value / token_value
    result = angus_tokens
    return result

print(solution())