def solution():
    """In 2021, Wayne is 37 years old.  His brother Peter is 3 years older than him and their sister Julia is 2 years older than Peter.  What year was Julia born in?"""
    # Calculate the birth year of Wayne
    wayne_birth_year = 2021 - 37

    # Calculate the birth year of Peter
    peter_age = 37 + 3
    peter_birth_year = 2021 - peter_age

    # Calculate the birth year of Julia
    julia_age = peter_age + 2
    julia_birth_year = 2021 - julia_age

    # Display the birth year of Julia
    result = julia_birth_year
    return result

print(solution())