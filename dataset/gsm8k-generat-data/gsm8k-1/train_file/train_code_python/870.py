def solution():
    """In 2021, Wayne is 37 years old. His brother Peter is 3 years older than him and their sister Julia is 2 years older than Peter. What year was Julia born in?"""
    wayne_age = 37
    peter_age = wayne_age + 3
    julia_age = peter_age + 2
    current_year = 2021
    julia_birth_year = current_year - julia_age
    
    result = julia_birth_year
    
    return result

print(solution())