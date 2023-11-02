def solution():
    birth_of_venus_year = 1486
    public_domain_cutoff = 1923
    if birth_of_venus_year < public_domain_cutoff:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())