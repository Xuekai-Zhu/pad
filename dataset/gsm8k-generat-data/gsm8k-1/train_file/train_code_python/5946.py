def solution():
    """Karina was born in 1970 and she is currently twice as old as her brother. If her current age is 40, in what year was her brother born?"""
    karina_age = 40
    karina_birth_year = 1970
    brother_age = karina_age / 2
    brother_birth_year = karina_birth_year + karina_age - brother_age
    result = brother_birth_year
    return result

print(solution())