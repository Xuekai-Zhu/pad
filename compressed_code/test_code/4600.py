def solution():
    
    karina_birth_year = 1970
    karina_age = 40
    brother_age = karina_age / 2
    brother_birth_year = karina_birth_year + karina_age - brother_age
    result = brother_birth_year
    return result

print(solution())