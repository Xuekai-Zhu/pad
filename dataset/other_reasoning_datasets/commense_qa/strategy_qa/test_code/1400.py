def solution():
    baker_dozen = 13
    alan_birth_year = 1926
    current_year = 2020
    age = current_year - alan_birth_year
    presidents = 16
    if presidents >= baker_dozen and age > baker_dozen:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())