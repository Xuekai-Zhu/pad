def solution():
    current_year = 2021
    Godzilla_release_year = 1954
    public_domain_year = 2049
    if current_year < public_domain_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())