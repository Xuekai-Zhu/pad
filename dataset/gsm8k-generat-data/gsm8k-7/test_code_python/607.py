def solution():
    num_tokens = 1000000
    num_siblings = 4

    # Calculate the number of tokens Sandy will keep for herself
    sandy_tokens = num_tokens / 2

    # Calculate the number of tokens each sibling will receive
    sibling_tokens = (num_tokens - sandy_tokens) / num_siblings

    # Calculate the difference in tokens between Sandy and each sibling
    difference = sandy_tokens - sibling_tokens
    result = difference
    return result

print(solution())