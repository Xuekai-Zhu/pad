def solution():
    wayne_age = 37
    peter_age = wayne_age - 3
    julia_age = peter_age + 2
    current_year = 2021

    # Calculate the year Julia was born
    julia_birth_year = current_year - julia_age
    result = julia_birth_year
    return result

print(solution())