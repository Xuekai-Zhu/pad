def solution():
    # Define Oscar Wilde's situation and the current law in the US regarding homosexuality
    oscar_wilde_imprisoned = True
    homosexuality_legal_in_US = True
    # Check if Oscar Wilde's treatment would be considered fair under current US law
    if oscar_wilde_imprisoned and not homosexuality_legal_in_US:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())