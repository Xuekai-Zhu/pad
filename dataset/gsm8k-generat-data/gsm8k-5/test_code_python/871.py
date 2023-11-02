def solution():
    wayne_age = 37  # Wayne's age in 2021
    peter_age = wayne_age + 3  # Peter is 3 years older than Wayne
    julia_age = peter_age + 2  # Julia is 2 years older than Peter
    current_year = 2021  # Current year is 2021

    # Calculate the year Julia was born in
    julia_birth_year = current_year - julia_age
    result = julia_birth_year
    return result

print(solution())