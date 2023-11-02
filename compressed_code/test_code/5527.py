def solution():
    
    elsa_tokens = 60
    token_value = 4
    elsa_value = elsa_tokens * token_value
    angus_value = elsa_value - 20
    angus_tokens = angus_value / token_value
    result = angus_tokens
    return result

print(solution())