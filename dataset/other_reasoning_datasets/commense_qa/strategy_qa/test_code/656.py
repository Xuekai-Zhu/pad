def solution():
    # Define the effects of embalming fluid on the body
    embalmed_body = "firm"
    non_embalmed_body = "soft"
    # Check if embalmed bodies feel different at funerals
    if embalmed_body != non_embalmed_body:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())